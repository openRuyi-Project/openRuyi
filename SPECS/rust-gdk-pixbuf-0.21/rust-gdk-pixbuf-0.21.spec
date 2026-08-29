# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gdk-pixbuf
%global full_version 0.21.5
%global pkgname gdk-pixbuf-0.21

Name:           rust-gdk-pixbuf-0.21
Version:        0.21.5
Release:        %autorelease
Summary:        Rust crate "gdk-pixbuf"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:debb0d39e3cdd84626edfd54d6e4a6ba2da9a0ef2e796e691c4e9f8646fda00c
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gdk-pixbuf-sys-0.21/default) >= 0.21.0
Requires:       crate(gio-0.21/default) >= 0.21.0
Requires:       crate(glib-0.21/default) >= 0.21.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gdk-pixbuf"

%package     -n %{name}+v2-40
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_40"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.21/v2-40) >= 0.21.0
Provides:       crate(%{pkgname}/v2-40) = %{version}

%description -n %{name}+v2-40
This metapackage enables feature "v2_40" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-42
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_42"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-40) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.21/v2-42) >= 0.21.0
Provides:       crate(%{pkgname}/v2-42) = %{version}

%description -n %{name}+v2-42
This metapackage enables feature "v2_42" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2-44
Summary:        Rust bindings for the GdkPixbuf library - feature "v2_44"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v2-42) = %{version}
Requires:       crate(gdk-pixbuf-sys-0.21/v2-44) >= 0.21.0
Provides:       crate(%{pkgname}/v2-44) = %{version}

%description -n %{name}+v2-44
This metapackage enables feature "v2_44" for the Rust gdk-pixbuf crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
