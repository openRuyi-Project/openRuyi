# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff
%global full_version 0.2.24
%global pkgname jiff-0.2

Name:           rust-jiff-0.2
Version:        0.2.24
Release:        %autorelease
Summary:        Rust crate "jiff"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff
#!RemoteAsset:  sha256:f00b5dbd620d61dfdcb6007c9c1f6054ebd75319f163d886a9055cec1155073d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jiff-static-0.2/default) >= 0.2.24
Requires:       crate(portable-atomic-1) >= 1.10.0
Requires:       crate(portable-atomic-util-0.2) >= 0.2.4
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/perf-inline) = %{version}

%description
This library is heavily inspired by the Temporal project.
Source code for takopackized Rust crate "jiff"

%package     -n %{name}+alloc
Summary:        Date-time library that encourages you to jump into the pit of success - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.4
Requires:       crate(serde-core-1/alloc) >= 1.0.221
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This library is heavily inspired by the Temporal project.
This metapackage enables feature "alloc" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Date-time library that encourages you to jump into the pit of success - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/perf-inline) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tz-fat) = %{version}
Requires:       crate(%{pkgname}/tz-system) = %{version}
Requires:       crate(%{pkgname}/tzdb-bundle-platform) = %{version}
Requires:       crate(%{pkgname}/tzdb-concatenated) = %{version}
Requires:       crate(%{pkgname}/tzdb-zoneinfo) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This library is heavily inspired by the Temporal project.
This metapackage enables feature "default" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Date-time library that encourages you to jump into the pit of success - feature "js"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(js-sys-0.3/default) >= 0.3.50
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.70
Provides:       crate(%{pkgname}/js) = %{version}

%description -n %{name}+js
This library is heavily inspired by the Temporal project.
This metapackage enables feature "js" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Date-time library that encourages you to jump into the pit of success - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4) >= 0.4.21
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This library is heavily inspired by the Temporal project.
This metapackage enables feature "logging" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date-time library that encourages you to jump into the pit of success - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-core-1) >= 1.0.221
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This library is heavily inspired by the Temporal project.
This metapackage enables feature "serde" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Date-time library that encourages you to jump into the pit of success - feature "static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/static-tz) = %{version}
Requires:       crate(jiff-static-0.2/tzdb) >= 0.2.24
Provides:       crate(%{pkgname}/static) = %{version}

%description -n %{name}+static
This library is heavily inspired by the Temporal project.
This metapackage enables feature "static" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static-tz
Summary:        Date-time library that encourages you to jump into the pit of success - feature "static-tz"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-static-0.2/default) >= 0.2.24
Provides:       crate(%{pkgname}/static-tz) = %{version}

%description -n %{name}+static-tz
This library is heavily inspired by the Temporal project.
This metapackage enables feature "static-tz" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Date-time library that encourages you to jump into the pit of success - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(log-0.4/std) >= 0.4.21
Requires:       crate(serde-core-1/std) >= 1.0.221
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/tzdb-concatenated) = %{version}
Provides:       crate(%{pkgname}/tzdb-zoneinfo) = %{version}

%description -n %{name}+std
This library is heavily inspired by the Temporal project.
This metapackage enables feature "std" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tzdb-concatenated", and "tzdb-zoneinfo" features.

%package     -n %{name}+tz-fat
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tz-fat"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jiff-static-0.2/tz-fat) >= 0.2.24
Provides:       crate(%{pkgname}/tz-fat) = %{version}

%description -n %{name}+tz-fat
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tz-fat" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tz-system
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tz-system"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-time) >= 0.52.0
Provides:       crate(%{pkgname}/tz-system) = %{version}

%description -n %{name}+tz-system
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tz-system" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tzdb-bundle-always
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tzdb-bundle-always"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tzdb-bundle-always) = %{version}

%description -n %{name}+tzdb-bundle-always
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tzdb-bundle-always" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tzdb-bundle-platform
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tzdb-bundle-platform"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(jiff-tzdb-platform-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}/tzdb-bundle-platform) = %{version}

%description -n %{name}+tzdb-bundle-platform
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tzdb-bundle-platform" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
