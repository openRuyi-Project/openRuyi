# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pango
%global full_version 0.22.6
%global pkgname pango-0.22

Name:           rust-pango-0.22
Version:        0.22.6
Release:        %autorelease
Summary:        Rust crate "pango"
License:        MIT
URL:            https://gtk-rs.org/
#!RemoteAsset:  sha256:251bdc6e6487b811be0e406a21e301e07e45c0aa8fa39e00c0c8e12a91752438
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gio-0.22/default) >= 0.22.0
Requires:       crate(glib-0.22) >= 0.22.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(pango-sys-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "pango"

%package     -n %{name}+v1-42
Summary:        Rust bindings for the Pango library - feature "v1_42"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pango-sys-0.22/v1-42) >= 0.22.0
Provides:       crate(%{pkgname}/v1-42) = %{version}

%description -n %{name}+v1-42
This metapackage enables feature "v1_42" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-44
Summary:        Rust bindings for the Pango library - feature "v1_44"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-42) = %{version}
Requires:       crate(pango-sys-0.22/v1-44) >= 0.22.0
Provides:       crate(%{pkgname}/v1-44) = %{version}

%description -n %{name}+v1-44
This metapackage enables feature "v1_44" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-46
Summary:        Rust bindings for the Pango library - feature "v1_46"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-44) = %{version}
Requires:       crate(pango-sys-0.22/v1-46) >= 0.22.0
Provides:       crate(%{pkgname}/v1-46) = %{version}

%description -n %{name}+v1-46
This metapackage enables feature "v1_46" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-48
Summary:        Rust bindings for the Pango library - feature "v1_48"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-46) = %{version}
Requires:       crate(pango-sys-0.22/v1-48) >= 0.22.0
Provides:       crate(%{pkgname}/v1-48) = %{version}

%description -n %{name}+v1-48
This metapackage enables feature "v1_48" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-50
Summary:        Rust bindings for the Pango library - feature "v1_50"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-48) = %{version}
Requires:       crate(pango-sys-0.22/v1-50) >= 0.22.0
Provides:       crate(%{pkgname}/v1-50) = %{version}

%description -n %{name}+v1-50
This metapackage enables feature "v1_50" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-52
Summary:        Rust bindings for the Pango library - feature "v1_52"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-50) = %{version}
Requires:       crate(pango-sys-0.22/v1-52) >= 0.22.0
Provides:       crate(%{pkgname}/v1-52) = %{version}

%description -n %{name}+v1-52
This metapackage enables feature "v1_52" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-54
Summary:        Rust bindings for the Pango library - feature "v1_54"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-52) = %{version}
Requires:       crate(pango-sys-0.22/v1-54) >= 0.22.0
Provides:       crate(%{pkgname}/v1-54) = %{version}

%description -n %{name}+v1-54
This metapackage enables feature "v1_54" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-56
Summary:        Rust bindings for the Pango library - feature "v1_56"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-54) = %{version}
Requires:       crate(pango-sys-0.22/v1-56) >= 0.22.0
Provides:       crate(%{pkgname}/v1-56) = %{version}

%description -n %{name}+v1-56
This metapackage enables feature "v1_56" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v1-57
Summary:        Rust bindings for the Pango library - feature "v1_57"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/v1-56) = %{version}
Requires:       crate(pango-sys-0.22/v1-57) >= 0.22.0
Provides:       crate(%{pkgname}/v1-57) = %{version}

%description -n %{name}+v1-57
This metapackage enables feature "v1_57" for the Rust pango crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
