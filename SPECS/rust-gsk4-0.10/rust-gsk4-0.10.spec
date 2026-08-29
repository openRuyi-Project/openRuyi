# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gsk4
%global full_version 0.10.3
%global pkgname gsk4-0.10

Name:           rust-gsk4-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "gsk4"
License:        MIT
URL:            https://gtk-rs.org/gtk4-rs
#!RemoteAsset:  sha256:e755de9d8c5896c5beaa028b89e1969d067f1b9bf1511384ede971f5983aa153
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cairo-rs-0.21/default) >= 0.21.0
Requires:       crate(cairo-rs-0.21/use-glib) >= 0.21.0
Requires:       crate(gdk4-0.10/default) >= 0.10.0
Requires:       crate(glib-0.21/default) >= 0.21.0
Requires:       crate(glib-0.21/v2-66) >= 0.21.0
Requires:       crate(graphene-rs-0.21/default) >= 0.21.0
Requires:       crate(gsk4-sys-0.10/default) >= 0.10.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-0.21/default) >= 0.21.0
Requires:       crate(pango-0.21/v1-46) >= 0.21.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gsk4"

%package     -n %{name}+broadway
Summary:        Rust bindings of the GSK 4 library - feature "broadway"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gsk4-sys-0.10/broadway) >= 0.10.0
Provides:       crate(%{pkgname}/broadway) = %{version}

%description -n %{name}+broadway
This metapackage enables feature "broadway" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-10
Summary:        Rust bindings of the GSK 4 library - feature "v4_10"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-6) = %{version}
Requires:       crate(gdk4-0.10/v4-10) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-10) >= 0.10.0
Provides:       crate(%{pkgname}/v4-10) = %{version}

%description -n %{name}+v4-10
This metapackage enables feature "v4_10" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-14
Summary:        Rust bindings of the GSK 4 library - feature "v4_14"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-10) = %{version}
Requires:       crate(gdk4-0.10/v4-14) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-14) >= 0.10.0
Provides:       crate(%{pkgname}/v4-14) = %{version}

%description -n %{name}+v4-14
This metapackage enables feature "v4_14" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-16
Summary:        Rust bindings of the GSK 4 library - feature "v4_16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-14) = %{version}
Requires:       crate(gdk4-0.10/v4-16) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-16) >= 0.10.0
Provides:       crate(%{pkgname}/v4-16) = %{version}

%description -n %{name}+v4-16
This metapackage enables feature "v4_16" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-18
Summary:        Rust bindings of the GSK 4 library - feature "v4_18"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-16) = %{version}
Requires:       crate(gdk4-0.10/v4-18) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-18) >= 0.10.0
Provides:       crate(%{pkgname}/v4-18) = %{version}

%description -n %{name}+v4-18
This metapackage enables feature "v4_18" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-2
Summary:        Rust bindings of the GSK 4 library - feature "v4_2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gdk4-0.10/v4-2) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-2) >= 0.10.0
Provides:       crate(%{pkgname}/v4-2) = %{version}

%description -n %{name}+v4-2
This metapackage enables feature "v4_2" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-20
Summary:        Rust bindings of the GSK 4 library - feature "v4_20"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-18) = %{version}
Requires:       crate(gdk4-0.10/v4-20) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-20) >= 0.10.0
Provides:       crate(%{pkgname}/v4-20) = %{version}

%description -n %{name}+v4-20
This metapackage enables feature "v4_20" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-4
Summary:        Rust bindings of the GSK 4 library - feature "v4_4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-2) = %{version}
Requires:       crate(gdk4-0.10/v4-4) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-4) >= 0.10.0
Provides:       crate(%{pkgname}/v4-4) = %{version}

%description -n %{name}+v4-4
This metapackage enables feature "v4_4" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v4-6
Summary:        Rust bindings of the GSK 4 library - feature "v4_6"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v4-4) = %{version}
Requires:       crate(gdk4-0.10/v4-6) >= 0.10.0
Requires:       crate(gsk4-sys-0.10/v4-6) >= 0.10.0
Provides:       crate(%{pkgname}/v4-6) = %{version}

%description -n %{name}+v4-6
This metapackage enables feature "v4_6" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vulkan
Summary:        Rust bindings of the GSK 4 library - feature "vulkan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gsk4-sys-0.10/vulkan) >= 0.10.0
Provides:       crate(%{pkgname}/vulkan) = %{version}

%description -n %{name}+vulkan
This metapackage enables feature "vulkan" for the Rust gsk4 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
