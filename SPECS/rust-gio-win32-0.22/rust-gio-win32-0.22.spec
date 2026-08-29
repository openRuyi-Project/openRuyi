# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gio-win32
%global full_version 0.22.6
%global pkgname gio-win32-0.22

Name:           rust-gio-win32-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "gio-win32"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:bbb6cc4a9cfd946f4320d2e424c71a6d12e0791d1973f68457e2c39fb06e2880
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gio-0.22/default) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gio-win32"

%package     -n %{name}+v2-58
Summary:        Rust bindings for the GioWin32 library - feature "v2_58"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gio-0.22/v2-58) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-82) >= 0.22.0
Provides:       crate(%{pkgname}/v2-58) = %{version}

%description -n %{name}+v2-58
This metapackage enables feature "v2_58" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-60
Summary:        Rust bindings for the GioWin32 library - feature "v2_60"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-58) = %{version}
Requires:       crate(gio-0.22/v2-60) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-60) >= 0.22.0
Provides:       crate(%{pkgname}/v2-60) = %{version}

%description -n %{name}+v2-60
This metapackage enables feature "v2_60" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-66
Summary:        Rust bindings for the GioWin32 library - feature "v2_66"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-60) = %{version}
Requires:       crate(gio-0.22/v2-66) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-66) >= 0.22.0
Provides:       crate(%{pkgname}/v2-66) = %{version}

%description -n %{name}+v2-66
This metapackage enables feature "v2_66" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-78
Summary:        Rust bindings for the GioWin32 library - feature "v2_78"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-60) = %{version}
Requires:       crate(gio-0.22/v2-78) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-78) >= 0.22.0
Provides:       crate(%{pkgname}/v2-78) = %{version}

%description -n %{name}+v2-78
This metapackage enables feature "v2_78" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-82
Summary:        Rust bindings for the GioWin32 library - feature "v2_82"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-78) = %{version}
Requires:       crate(gio-0.22/v2-82) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-82) >= 0.22.0
Provides:       crate(%{pkgname}/v2-82) = %{version}

%description -n %{name}+v2-82
This metapackage enables feature "v2_82" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-84
Summary:        Rust bindings for the GioWin32 library - feature "v2_84"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-82) = %{version}
Requires:       crate(gio-0.22/v2-84) >= 0.22.0
Requires:       crate(gio-win32-sys-0.22/v2-84) >= 0.22.0
Provides:       crate(%{pkgname}/v2-84) = %{version}

%description -n %{name}+v2-84
This metapackage enables feature "v2_84" for the Rust gio-win32 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
