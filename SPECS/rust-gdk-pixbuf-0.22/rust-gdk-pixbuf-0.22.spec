# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdk-pixbuf
%global full_version 0.22.0
%global pkgname gdk-pixbuf-0.22

Name:           rust-gdk-pixbuf-0.22
Version:        0.22.0
Release:        %autorelease
Summary:        Rust crate "gdk-pixbuf"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:25f420376dbee041b2db374ce4573892a36222bb3f6c0c43e24f0d67eae9b646
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gdk-pixbuf-sys-0.22/default) >= 0.22.0
Requires:       crate(gio-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gdk-pixbuf"

%package     -n %{name}+v2-40
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_40"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.22/v2-40) >= 0.22.0
Provides:       crate(%{pkgname}/v2-40) = %{version}

%description -n %{name}+v2-40
This metapackage enables feature "v2_40" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-42
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_42"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-40) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.22/v2-42) >= 0.22.0
Provides:       crate(%{pkgname}/v2-42) = %{version}

%description -n %{name}+v2-42
This metapackage enables feature "v2_42" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-44
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_44"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-42) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.22/v2-44) >= 0.22.0
Provides:       crate(%{pkgname}/v2-44) = %{version}

%description -n %{name}+v2-44
This metapackage enables feature "v2_44" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
