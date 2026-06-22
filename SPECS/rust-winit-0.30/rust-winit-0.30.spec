# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name winit
%global full_version 0.30.13
%global pkgname winit-0.30

Name:           rust-winit-0.30
Version:        0.30.13
Release:        %autorelease
Summary:        Rust crate "winit"
License:        Apache-2.0
URL:            https://github.com/rust-windowing/winit
#!RemoteAsset:  sha256:a6755fa58a9f8350bd1e472d4c3fcc25f824ec358933bba33306d0b63df5978d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(android-activity-0.6/default) >= 0.6.0
Requires:       crate(atomic-waker-1/default) >= 1.0.0
Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(block2-0.5/default) >= 0.5.1
Requires:       crate(calloop-0.13/default) >= 0.13.0
Requires:       crate(cfg-aliases-0.2) >= 0.2.1
Requires:       crate(concurrent-queue-2) >= 2.0.0
Requires:       crate(core-foundation-0.9/default) >= 0.9.3
Requires:       crate(core-graphics-0.23/default) >= 0.23.1
Requires:       crate(cursor-icon-1/default) >= 1.1.0
Requires:       crate(dpi-0.1/default) >= 0.1.1
Requires:       crate(js-sys-0.3/default) >= 0.3.70
Requires:       crate(libc-0.2/default) >= 0.2.64
Requires:       crate(ndk-0.9) >= 0.9.0
Requires:       crate(objc2-0.5/default) >= 0.5.2
Requires:       crate(objc2-0.5/relax-sign-encoding) >= 0.5.2
Requires:       crate(objc2-app-kit-0.2/default) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsappearance) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsapplication) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsbitmapimagerep) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsbutton) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nscolor) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nscontrol) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nscursor) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsdragging) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsevent) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsgraphics) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsgraphicscontext) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsimage) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsimagerep) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsmenu) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsmenuitem) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsopenglview) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nspasteboard) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsresponder) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsrunningapplication) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsscreen) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nstextinputclient) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nstextinputcontext) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nsview) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nswindow) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nswindowscripting) >= 0.2.2
Requires:       crate(objc2-app-kit-0.2/nswindowtabgroup) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/default) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/dispatch) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdistributednotificationcenter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nskeyvalueobserving) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspathutilities) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsprocessinfo) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrunloop) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsthread) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/default) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiapplication) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uidevice) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uievent) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uigeometry) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uigesturerecognizer) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiorientation) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uipangesturerecognizer) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uipinchgesturerecognizer) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiresponder) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uirotationgesturerecognizer) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiscreen) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiscreenmode) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uitapgesturerecognizer) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uitextinput) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uitextinputtraits) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uitouch) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uitraitcollection) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiview) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiviewcontroller) >= 0.2.2
Requires:       crate(objc2-ui-kit-0.2/uiwindow) >= 0.2.2
Requires:       crate(orbclient-0.3) >= 0.3.47
Requires:       crate(pin-project-1/default) >= 1.0.0
Requires:       crate(redox-syscall-0.4/default) >= 0.4.1
Requires:       crate(rustix-0.38/process) >= 0.38.4
Requires:       crate(rustix-0.38/std) >= 0.38.4
Requires:       crate(rustix-0.38/system) >= 0.38.4
Requires:       crate(rustix-0.38/thread) >= 0.38.4
Requires:       crate(smol-str-0.2/default) >= 0.2.0
Requires:       crate(tracing-0.1) >= 0.1.40
Requires:       crate(unicode-segmentation-1/default) >= 1.7.1
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.93
Requires:       crate(wasm-bindgen-futures-0.4/default) >= 0.4.43
Requires:       crate(web-sys-0.3/abortcontroller) >= 0.3.70
Requires:       crate(web-sys-0.3/abortsignal) >= 0.3.70
Requires:       crate(web-sys-0.3/blob) >= 0.3.70
Requires:       crate(web-sys-0.3/blobpropertybag) >= 0.3.70
Requires:       crate(web-sys-0.3/console) >= 0.3.70
Requires:       crate(web-sys-0.3/cssstyledeclaration) >= 0.3.70
Requires:       crate(web-sys-0.3/default) >= 0.3.70
Requires:       crate(web-sys-0.3/document) >= 0.3.70
Requires:       crate(web-sys-0.3/domexception) >= 0.3.70
Requires:       crate(web-sys-0.3/domrect) >= 0.3.70
Requires:       crate(web-sys-0.3/domrectreadonly) >= 0.3.70
Requires:       crate(web-sys-0.3/element) >= 0.3.70
Requires:       crate(web-sys-0.3/event) >= 0.3.70
Requires:       crate(web-sys-0.3/eventtarget) >= 0.3.70
Requires:       crate(web-sys-0.3/focusevent) >= 0.3.70
Requires:       crate(web-sys-0.3/htmlcanvaselement) >= 0.3.70
Requires:       crate(web-sys-0.3/htmlelement) >= 0.3.70
Requires:       crate(web-sys-0.3/htmlimageelement) >= 0.3.70
Requires:       crate(web-sys-0.3/imagebitmap) >= 0.3.70
Requires:       crate(web-sys-0.3/imagebitmapoptions) >= 0.3.70
Requires:       crate(web-sys-0.3/imagebitmaprenderingcontext) >= 0.3.70
Requires:       crate(web-sys-0.3/imagedata) >= 0.3.70
Requires:       crate(web-sys-0.3/intersectionobserver) >= 0.3.70
Requires:       crate(web-sys-0.3/intersectionobserverentry) >= 0.3.70
Requires:       crate(web-sys-0.3/keyboardevent) >= 0.3.70
Requires:       crate(web-sys-0.3/mediaquerylist) >= 0.3.70
Requires:       crate(web-sys-0.3/messagechannel) >= 0.3.70
Requires:       crate(web-sys-0.3/messageport) >= 0.3.70
Requires:       crate(web-sys-0.3/navigator) >= 0.3.70
Requires:       crate(web-sys-0.3/node) >= 0.3.70
Requires:       crate(web-sys-0.3/orientationlocktype) >= 0.3.70
Requires:       crate(web-sys-0.3/orientationtype) >= 0.3.70
Requires:       crate(web-sys-0.3/pagetransitionevent) >= 0.3.70
Requires:       crate(web-sys-0.3/permissions) >= 0.3.70
Requires:       crate(web-sys-0.3/permissionstate) >= 0.3.70
Requires:       crate(web-sys-0.3/permissionstatus) >= 0.3.70
Requires:       crate(web-sys-0.3/pointerevent) >= 0.3.70
Requires:       crate(web-sys-0.3/premultiplyalpha) >= 0.3.70
Requires:       crate(web-sys-0.3/resizeobserver) >= 0.3.70
Requires:       crate(web-sys-0.3/resizeobserverboxoptions) >= 0.3.70
Requires:       crate(web-sys-0.3/resizeobserverentry) >= 0.3.70
Requires:       crate(web-sys-0.3/resizeobserveroptions) >= 0.3.70
Requires:       crate(web-sys-0.3/resizeobserversize) >= 0.3.70
Requires:       crate(web-sys-0.3/screen) >= 0.3.70
Requires:       crate(web-sys-0.3/screenorientation) >= 0.3.70
Requires:       crate(web-sys-0.3/url) >= 0.3.70
Requires:       crate(web-sys-0.3/visibilitystate) >= 0.3.70
Requires:       crate(web-sys-0.3/wheelevent) >= 0.3.70
Requires:       crate(web-sys-0.3/window) >= 0.3.70
Requires:       crate(web-sys-0.3/worker) >= 0.3.70
Requires:       crate(web-time-1/default) >= 1.0.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-devices-humaninterfacedevice) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-globalization) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-graphics-dwm) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-graphics-gdi) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-media) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-security) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-com) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-com-structuredstorage) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-libraryloader) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-ole) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-systeminformation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-systemservices) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-threading) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-windowsprogramming) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-accessibility) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-controls) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-hidpi) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-input-ime) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-input-keyboardandmouse) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-input-pointer) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-input-touch) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-shell) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-textservices) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-ui-windowsandmessaging) >= 0.52.0
Requires:       crate(xkbcommon-dl-0.4/default) >= 0.4.2
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "winit"

%package     -n %{name}+ahash
Summary:        Cross-platform window creation library - feature "ahash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ahash-0.8/default) >= 0.8.7
Requires:       crate(ahash-0.8/no-rng) >= 0.8.7
Provides:       crate(%{pkgname}/ahash) = %{version}

%description -n %{name}+ahash
This metapackage enables feature "ahash" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+android-game-activity
Summary:        Cross-platform window creation library - feature "android-game-activity"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(android-activity-0.6/game-activity) >= 0.6.0
Provides:       crate(%{pkgname}/android-game-activity) = %{version}

%description -n %{name}+android-game-activity
This metapackage enables feature "android-game-activity" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+android-native-activity
Summary:        Cross-platform window creation library - feature "android-native-activity"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(android-activity-0.6/native-activity) >= 0.6.0
Provides:       crate(%{pkgname}/android-native-activity) = %{version}

%description -n %{name}+android-native-activity
This metapackage enables feature "android-native-activity" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Cross-platform window creation library - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1) >= 1.13.1
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Cross-platform window creation library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rwh-06) = %{version}
Requires:       crate(%{pkgname}/wayland) = %{version}
Requires:       crate(%{pkgname}/wayland-csd-adwaita) = %{version}
Requires:       crate(%{pkgname}/wayland-dlopen) = %{version}
Requires:       crate(%{pkgname}/x11) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memmap2
Summary:        Cross-platform window creation library - feature "memmap2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memmap2-0.9/default) >= 0.9.0
Provides:       crate(%{pkgname}/memmap2) = %{version}

%description -n %{name}+memmap2
This metapackage enables feature "memmap2" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        Cross-platform window creation library - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dpi-0.1/mint) >= 0.1.1
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+percent-encoding
Summary:        Cross-platform window creation library - feature "percent-encoding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(percent-encoding-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/percent-encoding) = %{version}

%description -n %{name}+percent-encoding
This metapackage enables feature "percent-encoding" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-04
Summary:        Cross-platform window creation library - feature "rwh_04"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-0.9/rwh-04) >= 0.9.0
Requires:       crate(raw-window-handle-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/rwh-04) = %{version}

%description -n %{name}+rwh-04
This metapackage enables feature "rwh_04" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-05
Summary:        Cross-platform window creation library - feature "rwh_05"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-0.9/rwh-05) >= 0.9.0
Requires:       crate(raw-window-handle-0.5/default) >= 0.5.2
Requires:       crate(raw-window-handle-0.5/std) >= 0.5.2
Provides:       crate(%{pkgname}/rwh-05) = %{version}

%description -n %{name}+rwh-05
This metapackage enables feature "rwh_05" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rwh-06
Summary:        Cross-platform window creation library - feature "rwh_06"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ndk-0.9/rwh-06) >= 0.9.0
Requires:       crate(raw-window-handle-0.6/default) >= 0.6.0
Requires:       crate(raw-window-handle-0.6/std) >= 0.6.0
Provides:       crate(%{pkgname}/rwh-06) = %{version}

%description -n %{name}+rwh-06
This metapackage enables feature "rwh_06" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sctk
Summary:        Cross-platform window creation library - feature "sctk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smithay-client-toolkit-0.19/calloop) >= 0.19.2
Provides:       crate(%{pkgname}/sctk) = %{version}

%description -n %{name}+sctk
This metapackage enables feature "sctk" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sctk-adwaita
Summary:        Cross-platform window creation library - feature "sctk-adwaita" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sctk-adwaita-0.10) >= 0.10.1
Provides:       crate(%{pkgname}/sctk-adwaita) = %{version}
Provides:       crate(%{pkgname}/wayland-csd-adwaita-notitle) = %{version}

%description -n %{name}+sctk-adwaita
This metapackage enables feature "sctk-adwaita" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "wayland-csd-adwaita-notitle" feature.

%package     -n %{name}+serde
Summary:        Cross-platform window creation library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cursor-icon-1/serde) >= 1.1.0
Requires:       crate(dpi-0.1/serde) >= 0.1.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/serde-derive) >= 1.0.0
Requires:       crate(smol-str-0.2/serde) >= 0.2.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland
Summary:        Cross-platform window creation library - feature "wayland"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ahash) = %{version}
Requires:       crate(%{pkgname}/memmap2) = %{version}
Requires:       crate(%{pkgname}/sctk) = %{version}
Requires:       crate(%{pkgname}/wayland-backend) = %{version}
Requires:       crate(%{pkgname}/wayland-client) = %{version}
Requires:       crate(%{pkgname}/wayland-protocols) = %{version}
Requires:       crate(%{pkgname}/wayland-protocols-plasma) = %{version}
Provides:       crate(%{pkgname}/wayland) = %{version}

%description -n %{name}+wayland
This metapackage enables feature "wayland" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-backend
Summary:        Cross-platform window creation library - feature "wayland-backend"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/client-system) >= 0.3.10
Provides:       crate(%{pkgname}/wayland-backend) = %{version}

%description -n %{name}+wayland-backend
This metapackage enables feature "wayland-backend" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-client
Summary:        Cross-platform window creation library - feature "wayland-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-client-0.31/default) >= 0.31.10
Provides:       crate(%{pkgname}/wayland-client) = %{version}

%description -n %{name}+wayland-client
This metapackage enables feature "wayland-client" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-csd-adwaita
Summary:        Cross-platform window creation library - feature "wayland-csd-adwaita"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sctk-adwaita) = %{version}
Requires:       crate(sctk-adwaita-0.10/ab-glyph) >= 0.10.1
Provides:       crate(%{pkgname}/wayland-csd-adwaita) = %{version}

%description -n %{name}+wayland-csd-adwaita
This metapackage enables feature "wayland-csd-adwaita" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-csd-adwaita-crossfont
Summary:        Cross-platform window creation library - feature "wayland-csd-adwaita-crossfont"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/sctk-adwaita) = %{version}
Requires:       crate(sctk-adwaita-0.10/crossfont) >= 0.10.1
Provides:       crate(%{pkgname}/wayland-csd-adwaita-crossfont) = %{version}

%description -n %{name}+wayland-csd-adwaita-crossfont
This metapackage enables feature "wayland-csd-adwaita-crossfont" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-dlopen
Summary:        Cross-platform window creation library - feature "wayland-dlopen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-backend-0.3/client-system) >= 0.3.10
Requires:       crate(wayland-backend-0.3/dlopen) >= 0.3.10
Provides:       crate(%{pkgname}/wayland-dlopen) = %{version}

%description -n %{name}+wayland-dlopen
This metapackage enables feature "wayland-dlopen" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-protocols
Summary:        Cross-platform window creation library - feature "wayland-protocols"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-protocols-0.32/default) >= 0.32.8
Requires:       crate(wayland-protocols-0.32/staging) >= 0.32.8
Provides:       crate(%{pkgname}/wayland-protocols) = %{version}

%description -n %{name}+wayland-protocols
This metapackage enables feature "wayland-protocols" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wayland-protocols-plasma
Summary:        Cross-platform window creation library - feature "wayland-protocols-plasma"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(wayland-protocols-plasma-0.3/client) >= 0.3.8
Requires:       crate(wayland-protocols-plasma-0.3/default) >= 0.3.8
Provides:       crate(%{pkgname}/wayland-protocols-plasma) = %{version}

%description -n %{name}+wayland-protocols-plasma
This metapackage enables feature "wayland-protocols-plasma" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x11
Summary:        Cross-platform window creation library - feature "x11"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytemuck) = %{version}
Requires:       crate(%{pkgname}/percent-encoding) = %{version}
Requires:       crate(%{pkgname}/x11-dl) = %{version}
Requires:       crate(%{pkgname}/x11rb) = %{version}
Requires:       crate(xkbcommon-dl-0.4/x11) >= 0.4.2
Provides:       crate(%{pkgname}/x11) = %{version}

%description -n %{name}+x11
This metapackage enables feature "x11" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x11-dl
Summary:        Cross-platform window creation library - feature "x11-dl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11-dl-2/default) >= 2.19.1
Provides:       crate(%{pkgname}/x11-dl) = %{version}

%description -n %{name}+x11-dl
This metapackage enables feature "x11-dl" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x11rb
Summary:        Cross-platform window creation library - feature "x11rb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x11rb-0.13/allow-unsafe-code) >= 0.13.0
Requires:       crate(x11rb-0.13/dl-libxcb) >= 0.13.0
Requires:       crate(x11rb-0.13/randr) >= 0.13.0
Requires:       crate(x11rb-0.13/resource-manager) >= 0.13.0
Requires:       crate(x11rb-0.13/xinput) >= 0.13.0
Requires:       crate(x11rb-0.13/xkb) >= 0.13.0
Provides:       crate(%{pkgname}/x11rb) = %{version}

%description -n %{name}+x11rb
This metapackage enables feature "x11rb" for the Rust winit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
