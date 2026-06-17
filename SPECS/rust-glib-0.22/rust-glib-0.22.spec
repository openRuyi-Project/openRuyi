# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib
%global full_version 0.22.7
%global pkgname glib-0.22

Name:           rust-glib-0.22
Version:        0.22.7
Release:        %autorelease
Summary:        Rust crate "glib"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:c207e04e51605dcf7b2924c41591b3a10e1438eaac5bcf448fb91f325381104a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.10.0
Requires:       crate(glib-macros-0.22) >= 0.22.0
Requires:       crate(glib-sys-0.22/default) >= 0.22.0
Requires:       crate(gobject-sys-0.22/default) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(memchr-2/default) >= 2.8.0
Requires:       crate(smallvec-1/const-generics) >= 1.15.0
Requires:       crate(smallvec-1/const-new) >= 1.15.0
Requires:       crate(smallvec-1/default) >= 1.15.0
Requires:       crate(smallvec-1/union) >= 1.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compiletests) = %{version}

%description
Source code for takopackized Rust crate "glib"

%package     -n %{name}+default
Summary:        Rust bindings for the GLib library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/gio) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Rust bindings for the GLib library - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-channel) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/futures-executor) = %{version}
Requires:       crate(%{pkgname}/futures-task) = %{version}
Requires:       crate(%{pkgname}/futures-util) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-channel
Summary:        Rust bindings for the GLib library - feature "futures-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-channel) = %{version}

%description -n %{name}+futures-channel
This metapackage enables feature "futures-channel" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Rust bindings for the GLib library - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-executor
Summary:        Rust bindings for the GLib library - feature "futures-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-executor-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-executor) = %{version}

%description -n %{name}+futures-executor
This metapackage enables feature "futures-executor" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-task
Summary:        Rust bindings for the GLib library - feature "futures-task"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-task-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures-task) = %{version}

%description -n %{name}+futures-task
This metapackage enables feature "futures-task" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-util
Summary:        Rust bindings for the GLib library - feature "futures-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-util) = %{version}

%description -n %{name}+futures-util
This metapackage enables feature "futures-util" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gio
Summary:        Rust bindings for the GLib library - feature "gio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/gio-sys) = %{version}
Provides:       crate(%{pkgname}/gio) = %{version}

%description -n %{name}+gio
This metapackage enables feature "gio" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gio-sys
Summary:        Rust bindings for the GLib library - feature "gio-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-sys-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/gio-sys) = %{version}

%description -n %{name}+gio-sys
This metapackage enables feature "gio-sys" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log-kv
Summary:        Rust bindings for the GLib library - feature "log_kv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(log-0.4/kv) >= 0.4.0
Provides:       crate(%{pkgname}/log-kv) = %{version}

%description -n %{name}+log-kv
This metapackage enables feature "log_kv" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rs-log
Summary:        Rust bindings for the GLib library - feature "rs-log" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log) = %{version}
Provides:       crate(%{pkgname}/log-macros) = %{version}
Provides:       crate(%{pkgname}/rs-log) = %{version}

%description -n %{name}+rs-log
This metapackage enables feature "rs-log" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "log", and "log_macros" features.

%package     -n %{name}+v2-58
Summary:        Rust bindings for the GLib library - feature "v2_58"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(glib-sys-0.22/v2-58) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-58) >= 0.22.0
Provides:       crate(%{pkgname}/v2-58) = %{version}

%description -n %{name}+v2-58
This metapackage enables feature "v2_58" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-60
Summary:        Rust bindings for the GLib library - feature "v2_60"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-58) = %{version}
Requires:       crate(glib-sys-0.22/v2-60) >= 0.22.0
Provides:       crate(%{pkgname}/v2-60) = %{version}

%description -n %{name}+v2-60
This metapackage enables feature "v2_60" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-62
Summary:        Rust bindings for the GLib library - feature "v2_62"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-60) = %{version}
Requires:       crate(glib-sys-0.22/v2-62) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-62) >= 0.22.0
Provides:       crate(%{pkgname}/v2-62) = %{version}

%description -n %{name}+v2-62
This metapackage enables feature "v2_62" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-64
Summary:        Rust bindings for the GLib library - feature "v2_64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-62) = %{version}
Requires:       crate(glib-sys-0.22/v2-64) >= 0.22.0
Provides:       crate(%{pkgname}/v2-64) = %{version}

%description -n %{name}+v2-64
This metapackage enables feature "v2_64" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-66
Summary:        Rust bindings for the GLib library - feature "v2_66"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-64) = %{version}
Requires:       crate(glib-sys-0.22/v2-66) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-66) >= 0.22.0
Provides:       crate(%{pkgname}/v2-66) = %{version}

%description -n %{name}+v2-66
This metapackage enables feature "v2_66" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-68
Summary:        Rust bindings for the GLib library - feature "v2_68"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-66) = %{version}
Requires:       crate(glib-sys-0.22/v2-68) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-68) >= 0.22.0
Provides:       crate(%{pkgname}/v2-68) = %{version}

%description -n %{name}+v2-68
This metapackage enables feature "v2_68" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-70
Summary:        Rust bindings for the GLib library - feature "v2_70"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-68) = %{version}
Requires:       crate(glib-sys-0.22/v2-70) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-70) >= 0.22.0
Provides:       crate(%{pkgname}/v2-70) = %{version}

%description -n %{name}+v2-70
This metapackage enables feature "v2_70" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-72
Summary:        Rust bindings for the GLib library - feature "v2_72"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-70) = %{version}
Requires:       crate(glib-sys-0.22/v2-72) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-72) >= 0.22.0
Provides:       crate(%{pkgname}/v2-72) = %{version}

%description -n %{name}+v2-72
This metapackage enables feature "v2_72" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-74
Summary:        Rust bindings for the GLib library - feature "v2_74"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-72) = %{version}
Requires:       crate(glib-sys-0.22/v2-74) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-74) >= 0.22.0
Provides:       crate(%{pkgname}/v2-74) = %{version}

%description -n %{name}+v2-74
This metapackage enables feature "v2_74" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-76
Summary:        Rust bindings for the GLib library - feature "v2_76"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-74) = %{version}
Requires:       crate(glib-sys-0.22/v2-76) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-76) >= 0.22.0
Provides:       crate(%{pkgname}/v2-76) = %{version}

%description -n %{name}+v2-76
This metapackage enables feature "v2_76" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-78
Summary:        Rust bindings for the GLib library - feature "v2_78"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-76) = %{version}
Requires:       crate(glib-sys-0.22/v2-78) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-78) >= 0.22.0
Provides:       crate(%{pkgname}/v2-78) = %{version}

%description -n %{name}+v2-78
This metapackage enables feature "v2_78" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-80
Summary:        Rust bindings for the GLib library - feature "v2_80"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-78) = %{version}
Requires:       crate(glib-sys-0.22/v2-80) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-80) >= 0.22.0
Provides:       crate(%{pkgname}/v2-80) = %{version}

%description -n %{name}+v2-80
This metapackage enables feature "v2_80" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-82
Summary:        Rust bindings for the GLib library - feature "v2_82"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-80) = %{version}
Requires:       crate(glib-sys-0.22/v2-82) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-82) >= 0.22.0
Provides:       crate(%{pkgname}/v2-82) = %{version}

%description -n %{name}+v2-82
This metapackage enables feature "v2_82" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-84
Summary:        Rust bindings for the GLib library - feature "v2_84"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-82) = %{version}
Requires:       crate(glib-sys-0.22/v2-84) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-84) >= 0.22.0
Provides:       crate(%{pkgname}/v2-84) = %{version}

%description -n %{name}+v2-84
This metapackage enables feature "v2_84" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-86
Summary:        Rust bindings for the GLib library - feature "v2_86"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-84) = %{version}
Requires:       crate(glib-sys-0.22/v2-86) >= 0.22.0
Requires:       crate(gobject-sys-0.22/v2-86) >= 0.22.0
Provides:       crate(%{pkgname}/v2-86) = %{version}

%description -n %{name}+v2-86
This metapackage enables feature "v2_86" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-88
Summary:        Rust bindings for the GLib library - feature "v2_88"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-86) = %{version}
Requires:       crate(glib-sys-0.22/v2-88) >= 0.22.0
Provides:       crate(%{pkgname}/v2-88) = %{version}

%description -n %{name}+v2-88
This metapackage enables feature "v2_88" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-90
Summary:        Rust bindings for the GLib library - feature "v2_90"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-88) = %{version}
Requires:       crate(glib-sys-0.22/v2-90) >= 0.22.0
Provides:       crate(%{pkgname}/v2-90) = %{version}

%description -n %{name}+v2-90
This metapackage enables feature "v2_90" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
