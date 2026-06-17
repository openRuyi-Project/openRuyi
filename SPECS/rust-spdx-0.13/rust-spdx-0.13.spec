# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name spdx
%global full_version 0.13.4
%global pkgname spdx-0.13

Name:           rust-spdx-0.13
Version:        0.13.4
Release:        %autorelease
Summary:        Rust crate "spdx"
License:        Apache-2.0
URL:            https://github.com/EmbarkStudios/spdx
#!RemoteAsset:  sha256:a8da593e30beb790fc9424502eb898320b44e5eb30367dbda1c1edde8e2f32d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(smallvec-1/default) >= 1.15.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/text) = %{version}

%description
Source code for takopackized Rust crate "spdx"

%package     -n %{name}+detection
Summary:        Helper crate for SPDX expressions - feature "detection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/unicode-normalization) = %{version}
Provides:       crate(%{pkgname}/detection) = %{version}

%description -n %{name}+detection
This metapackage enables feature "detection" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detection-cache
Summary:        Helper crate for SPDX expressions - feature "detection-cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/detection) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/zstd) = %{version}
Provides:       crate(%{pkgname}/detection-cache) = %{version}

%description -n %{name}+detection-cache
This metapackage enables feature "detection-cache" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detection-inline-cache
Summary:        Helper crate for SPDX expressions - feature "detection-inline-cache"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/detection-cache) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/detection-inline-cache) = %{version}

%description -n %{name}+detection-inline-cache
This metapackage enables feature "detection-inline-cache" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+detection-parallel
Summary:        Helper crate for SPDX expressions - feature "detection-parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/detection) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/detection-parallel) = %{version}

%description -n %{name}+detection-parallel
This metapackage enables feature "detection-parallel" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Helper crate for SPDX expressions - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Helper crate for SPDX expressions - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/perf) >= 1.12.0
Requires:       crate(regex-1/unicode) >= 1.12.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Helper crate for SPDX expressions - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/perf) >= 1.12.0
Requires:       crate(regex-1/std) >= 1.12.0
Requires:       crate(regex-1/unicode) >= 1.12.0
Requires:       crate(unicode-normalization-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-normalization
Summary:        Helper crate for SPDX expressions - feature "unicode-normalization"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-normalization-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/unicode-normalization) = %{version}

%description -n %{name}+unicode-normalization
This metapackage enables feature "unicode-normalization" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zstd
Summary:        Helper crate for SPDX expressions - feature "zstd"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zstd-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/zstd) = %{version}

%description -n %{name}+zstd
This metapackage enables feature "zstd" for the Rust spdx crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
