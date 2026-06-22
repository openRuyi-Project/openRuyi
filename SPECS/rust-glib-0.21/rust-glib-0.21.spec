# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name glib
%global full_version 0.21.5
%global pkgname glib-0.21

Name:           rust-glib-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "glib"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:16de123c2e6c90ce3b573b7330de19be649080ec612033d397d72da265f1bd8b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.9.0
Requires:       crate(futures-channel-0.3/default) >= 0.3.0
Requires:       crate(futures-core-0.3) >= 0.3.0
Requires:       crate(futures-executor-0.3/default) >= 0.3.0
Requires:       crate(futures-task-0.3) >= 0.3.0
Requires:       crate(futures-util-0.3/default) >= 0.3.0
Requires:       crate(glib-macros-0.21/default) >= 0.21.0
Requires:       crate(glib-sys-0.21/default) >= 0.21.0
Requires:       crate(gobject-sys-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(memchr-2/default) >= 2.7.5
Requires:       crate(smallvec-1/const-generics) >= 1.15.0
Requires:       crate(smallvec-1/const-new) >= 1.15.0
Requires:       crate(smallvec-1/default) >= 1.15.0
Requires:       crate(smallvec-1/union) >= 1.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/compiletests) = %{version}

%description
Source code for takopackized Rust crate "glib"

%package     -n %{name}+gio-sys
Summary:        Rust bindings for the GLib library - feature "gio-sys" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-sys-0.21/default) >= 0.21.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/gio) = %{version}
Provides:       crate(%{pkgname}/gio-sys) = %{version}

%description -n %{name}+gio-sys
This metapackage enables feature "gio-sys" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "gio" features.

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
Requires:       crate(glib-sys-0.21/v2-58) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-58) >= 0.21.0
Provides:       crate(%{pkgname}/v2-58) = %{version}

%description -n %{name}+v2-58
This metapackage enables feature "v2_58" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-60
Summary:        Rust bindings for the GLib library - feature "v2_60"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-58) = %{version}
Requires:       crate(glib-sys-0.21/v2-60) >= 0.21.0
Provides:       crate(%{pkgname}/v2-60) = %{version}

%description -n %{name}+v2-60
This metapackage enables feature "v2_60" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-62
Summary:        Rust bindings for the GLib library - feature "v2_62"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-60) = %{version}
Requires:       crate(glib-sys-0.21/v2-62) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-62) >= 0.21.0
Provides:       crate(%{pkgname}/v2-62) = %{version}

%description -n %{name}+v2-62
This metapackage enables feature "v2_62" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-64
Summary:        Rust bindings for the GLib library - feature "v2_64"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-62) = %{version}
Requires:       crate(glib-sys-0.21/v2-64) >= 0.21.0
Provides:       crate(%{pkgname}/v2-64) = %{version}

%description -n %{name}+v2-64
This metapackage enables feature "v2_64" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-66
Summary:        Rust bindings for the GLib library - feature "v2_66"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-64) = %{version}
Requires:       crate(glib-sys-0.21/v2-66) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-66) >= 0.21.0
Provides:       crate(%{pkgname}/v2-66) = %{version}

%description -n %{name}+v2-66
This metapackage enables feature "v2_66" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-68
Summary:        Rust bindings for the GLib library - feature "v2_68"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-66) = %{version}
Requires:       crate(glib-sys-0.21/v2-68) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-68) >= 0.21.0
Provides:       crate(%{pkgname}/v2-68) = %{version}

%description -n %{name}+v2-68
This metapackage enables feature "v2_68" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-70
Summary:        Rust bindings for the GLib library - feature "v2_70"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-68) = %{version}
Requires:       crate(glib-sys-0.21/v2-70) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-70) >= 0.21.0
Provides:       crate(%{pkgname}/v2-70) = %{version}

%description -n %{name}+v2-70
This metapackage enables feature "v2_70" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-72
Summary:        Rust bindings for the GLib library - feature "v2_72"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-70) = %{version}
Requires:       crate(glib-sys-0.21/v2-72) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-72) >= 0.21.0
Provides:       crate(%{pkgname}/v2-72) = %{version}

%description -n %{name}+v2-72
This metapackage enables feature "v2_72" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-74
Summary:        Rust bindings for the GLib library - feature "v2_74"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-72) = %{version}
Requires:       crate(glib-sys-0.21/v2-74) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-74) >= 0.21.0
Provides:       crate(%{pkgname}/v2-74) = %{version}

%description -n %{name}+v2-74
This metapackage enables feature "v2_74" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-76
Summary:        Rust bindings for the GLib library - feature "v2_76"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-74) = %{version}
Requires:       crate(glib-sys-0.21/v2-76) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-76) >= 0.21.0
Provides:       crate(%{pkgname}/v2-76) = %{version}

%description -n %{name}+v2-76
This metapackage enables feature "v2_76" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-78
Summary:        Rust bindings for the GLib library - feature "v2_78"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-76) = %{version}
Requires:       crate(glib-sys-0.21/v2-78) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-78) >= 0.21.0
Provides:       crate(%{pkgname}/v2-78) = %{version}

%description -n %{name}+v2-78
This metapackage enables feature "v2_78" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-80
Summary:        Rust bindings for the GLib library - feature "v2_80"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-78) = %{version}
Requires:       crate(glib-sys-0.21/v2-80) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-80) >= 0.21.0
Provides:       crate(%{pkgname}/v2-80) = %{version}

%description -n %{name}+v2-80
This metapackage enables feature "v2_80" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-82
Summary:        Rust bindings for the GLib library - feature "v2_82"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-80) = %{version}
Requires:       crate(glib-sys-0.21/v2-82) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-82) >= 0.21.0
Provides:       crate(%{pkgname}/v2-82) = %{version}

%description -n %{name}+v2-82
This metapackage enables feature "v2_82" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-84
Summary:        Rust bindings for the GLib library - feature "v2_84"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-82) = %{version}
Requires:       crate(glib-sys-0.21/v2-84) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-84) >= 0.21.0
Provides:       crate(%{pkgname}/v2-84) = %{version}

%description -n %{name}+v2-84
This metapackage enables feature "v2_84" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-86
Summary:        Rust bindings for the GLib library - feature "v2_86"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-84) = %{version}
Requires:       crate(glib-sys-0.21/v2-86) >= 0.21.0
Requires:       crate(gobject-sys-0.21/v2-86) >= 0.21.0
Provides:       crate(%{pkgname}/v2-86) = %{version}

%description -n %{name}+v2-86
This metapackage enables feature "v2_86" for the Rust glib crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
