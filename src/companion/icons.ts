// One Material Symbols Sharp glyph per command, per field and per tab of the game's schema, keyed
// by the schema's identifiers (an identifier is never renamed). `fill` for a resource or an active
// state, line for a neutral pictogram (the game's rule). The glyphs the game's own screens already
// use keep their meaning: shield, favorite (hull), rocket_launch (engine), my_location (weapons),
// speed, bolt (energy), radar, straighten (distance), gamepad (controls help).
// Adding a command or a field: its line here, then `npm run symbols`; the tests fail on a miss.

import type { Icon } from "./render.js";

const line = (symbol: string): Icon => ({ symbol, fill: false });
const full = (symbol: string): Icon => ({ symbol, fill: true });

/** Commands that keep their label alone: no glyph says them better than their words. */
export const LABEL_ONLY = new Set(["target_squad_prev", "target_squad_next"]);

export const COMMAND_ICONS: Record<string, Icon> = {
	view_toggle: line("cameraswitch"), free_look: line("360"), zoom_toggle: line("zoom_in_map"),
	zoom_closer: line("zoom_in"), zoom_wider: line("zoom_out"), practice_panel: line("tune"),
	marker: line("bookmark_add"), fps_display: line("monitoring"), input_overlay: line("gamepad"),
	chat_open: line("chat"), race_restart: line("restart_alt"), race_abandon: line("flag"),
	race_trace_gate: line("route"), record_toggle: full("fiber_manual_record"),
	thrust_fwd: line("keyboard_double_arrow_up"), thrust_back: line("keyboard_double_arrow_down"),
	strafe_left: line("west"), strafe_right: line("east"), strafe_up: line("north"), strafe_down: line("south"),
	roll_left: line("rotate_left"), roll_right: line("rotate_right"),
	pitch_up: line("keyboard_arrow_up"), pitch_down: line("keyboard_arrow_down"),
	yaw_left: line("keyboard_arrow_left"), yaw_right: line("keyboard_arrow_right"),
	boost: line("fast_forward"), head_toggle: line("face"), head_center: line("recenter"),
	fire: line("my_location"), fire_group_1: line("looks_one"), fire_group_2: line("looks_two"),
	tri_weapons: full("my_location"), tri_engine: full("rocket_launch"), tri_shield: full("shield"),
	tri_neutral: line("balance"), capacitor_mode: line("battery_charging_full"), crosshair_color: line("palette"),
	conv_far: line("add"), conv_near: line("remove"), eject: line("eject"), self_destruct: line("dangerous"),
	duel: line("swords"), call_dismiss: line("call_end"),
	target_front: line("filter_center_focus"), target_subsystem: line("memory"), target_attacker: line("person_alert"),
	target_of_target: line("my_location"), target_prev: line("skip_previous"), target_next: line("skip_next"),
	target_clear: line("cancel"), target_mark: line("keep"),
	engine_toggle: line("rocket_launch"), headlights: line("flashlight_on"), cabin_light: line("light"),
	landing_gear: line("flight_land"), exit_ship: line("logout"), interact: line("touch_app"),
	station_menu: line("build"), turret_seat: line("event_seat"),
	tablet_focus: line("visibility"), tablet_up: line("arrow_upward"), tablet_down: line("arrow_downward"),
	tablet_left: line("arrow_back"), tablet_right: line("arrow_forward"), tablet_select: line("check"),
	tablet_back: line("undo"), tablet_tab_prev: line("chevron_left"), tablet_tab_next: line("chevron_right"),
	photo_mode: line("photo_camera"), photo_hide_ui: line("visibility_off"), photo_capture: line("screenshot_frame"),
	photo_slow: line("slow_motion_video"), photo_smooth_more: line("add"), photo_smooth_less: line("remove"),
	photo_speed_down: line("remove"), photo_speed_up: line("add"), photo_horizon: line("landscape"),
	photo_home: line("home"), photo_time: line("schedule"), photo_lock: line("lock"),
	photo_blur_less: line("blur_off"), photo_blur_more: line("blur_on"),
	photo_depth_less: line("remove"), photo_depth_more: line("add"),
	convergence_up: line("add"), convergence_down: line("remove"), convergence: line("center_focus_strong"),
};

export const FIELD_ICONS: Record<string, Icon> = {
	context: line("explore"), online: line("public"), head_tracking: line("face"),
	speed: line("speed"), throttle: line("equalizer"), boost: line("fast_forward"),
	energy_engine: full("rocket_launch"), energy_weapons: full("my_location"), energy_shield: full("shield"),
	hull: full("favorite"), station: full("ev_station"), engines: line("rocket_launch"),
	electronics: line("memory"), gear: line("flight_land"), headlights: line("flashlight_on"),
	cabin_light: line("light"), view_cockpit: line("videocam"), g: line("compress"), warp: line("cyclone"),
	convergence: line("center_focus_strong"), convergence_auto: line("center_focus_weak"),
	capacitor_full: full("battery_charging_full"), fire_group: line("layers"), charge: full("bolt"),
	beam: line("highlight"), target: line("filter_center_focus"), target_distance: line("straighten"),
	photo: line("photo_camera"), photo_focal: line("camera"), photo_smoothing: line("airwave"),
	photo_speed: line("speed"), photo_horizon: line("landscape"), photo_blur: line("blur_on"),
	photo_depth: line("straighten"), photo_frozen: line("ac_unit"),
};

/** The tabs of the game's Controls page: the folders of the profiles. */
export const TAB_ICONS: Record<string, Icon> = {
	"General": line("settings"), "Flight controls": line("flight"), "Combat": line("my_location"),
	"Ship commands": line("rocket"), "Head tracking": line("face"), "Tablet": line("visibility"),
	"Photo": line("photo_camera"), "Mouse": line("mouse"), "Turret": line("event_seat"), "Companion": line("gamepad"),
};

/** The keys of the profiles that are not in the schema, and the plugin's fixed pictures. */
export const NAV_ICONS: Record<string, Icon> = {
	back: line("arrow_back"), next: line("chevron_right"), idle: line("link_off"),
	command: line("touch_app"), value: line("speed"), plugin: line("rocket_launch"),
};

/** Every glyph the plugin ships: what tools/sync-symbols.mjs copies. */
export function allIcons(): Icon[] {
	return [COMMAND_ICONS, FIELD_ICONS, TAB_ICONS, NAV_ICONS].flatMap((table) => Object.values(table));
}

/** A command's pictogram, or null for a label alone (LABEL_ONLY, or an id the table does not know). */
export function commandIcon(id: string): Icon | null {
	return LABEL_ONLY.has(id) ? null : (COMMAND_ICONS[id] ?? null);
}

/** A field's pictogram, or null when the table does not know it. */
export function fieldIcon(id: string): Icon | null {
	return FIELD_ICONS[id] ?? null;
}
