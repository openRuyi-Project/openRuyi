# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jiff
%global full_version 0.2.23
%global pkgname jiff-0.2

Name:           rust-jiff-0.2
Version:        0.2.23
Release:        %autorelease
Summary:        Rust crate "jiff"
License:        Unlicense OR MIT
URL:            https://github.com/BurntSushi/jiff
#!RemoteAsset:  sha256:1a3546dc96b6d42c5f24902af9e2538e82e39ad350b0c766eb3fbf2d8f3d8359
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(jiff-static-0.2/default) >= 0.2.23
Requires:       crate(portable-atomic-1.0) >= 1.13.1
Requires:       crate(portable-atomic-util-0.2) >= 0.2.6
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/perf-inline)

%description
This library is heavily inspired by the Temporal project.
Source code for takopackized Rust crate "jiff"

%package     -n %{name}+alloc
Summary:        Date-time library that encourages you to jump into the pit of success - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(portable-atomic-util-0.2/alloc) >= 0.2.6
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This library is heavily inspired by the Temporal project.
This metapackage enables feature "alloc" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Date-time library that encourages you to jump into the pit of success - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/perf-inline)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/tz-fat)
Requires:       crate(%{pkgname}/tz-system)
Requires:       crate(%{pkgname}/tzdb-bundle-platform)
Requires:       crate(%{pkgname}/tzdb-concatenated)
Requires:       crate(%{pkgname}/tzdb-zoneinfo)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This library is heavily inspired by the Temporal project.
This metapackage enables feature "default" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+js
Summary:        Date-time library that encourages you to jump into the pit of success - feature "js"
Requires:       crate(%{pkgname})
Requires:       crate(js-sys-0.3/default) >= 0.3.50
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.70
Provides:       crate(%{pkgname}/js)

%description -n %{name}+js
This library is heavily inspired by the Temporal project.
This metapackage enables feature "js" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Date-time library that encourages you to jump into the pit of success - feature "logging"
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4) >= 0.4.29
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+logging
This library is heavily inspired by the Temporal project.
This metapackage enables feature "logging" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Date-time library that encourages you to jump into the pit of success - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This library is heavily inspired by the Temporal project.
This metapackage enables feature "serde" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static
Summary:        Date-time library that encourages you to jump into the pit of success - feature "static"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/static-tz)
Requires:       crate(jiff-static-0.2/tzdb) >= 0.2.23
Provides:       crate(%{pkgname}/static)

%description -n %{name}+static
This library is heavily inspired by the Temporal project.
This metapackage enables feature "static" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+static-tz
Summary:        Date-time library that encourages you to jump into the pit of success - feature "static-tz"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-static-0.2/default) >= 0.2.23
Provides:       crate(%{pkgname}/static-tz)

%description -n %{name}+static-tz
This library is heavily inspired by the Temporal project.
This metapackage enables feature "static-tz" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Date-time library that encourages you to jump into the pit of success - feature "std" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(log-0.4/std) >= 0.4.29
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/tzdb-concatenated)
Provides:       crate(%{pkgname}/tzdb-zoneinfo)

%description -n %{name}+std
This library is heavily inspired by the Temporal project.
This metapackage enables feature "std" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "tzdb-concatenated", and "tzdb-zoneinfo" features.

%package     -n %{name}+tz-fat
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tz-fat"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-static-0.2/tz-fat) >= 0.2.23
Provides:       crate(%{pkgname}/tz-fat)

%description -n %{name}+tz-fat
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tz-fat" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tz-system
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tz-system"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(windows-sys-0.61/win32-foundation) >= 0.61.2
Requires:       crate(windows-sys-0.61/win32-system-time) >= 0.61.2
Provides:       crate(%{pkgname}/tz-system)

%description -n %{name}+tz-system
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tz-system" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tzdb-bundle-always
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tzdb-bundle-always"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(jiff-tzdb-0.1/default) >= 0.1.6
Provides:       crate(%{pkgname}/tzdb-bundle-always)

%description -n %{name}+tzdb-bundle-always
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tzdb-bundle-always" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tzdb-bundle-platform
Summary:        Date-time library that encourages you to jump into the pit of success - feature "tzdb-bundle-platform"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(jiff-tzdb-platform-0.1/default) >= 0.1.3
Provides:       crate(%{pkgname}/tzdb-bundle-platform)

%description -n %{name}+tzdb-bundle-platform
This library is heavily inspired by the Temporal project.
This metapackage enables feature "tzdb-bundle-platform" for the Rust jiff crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
