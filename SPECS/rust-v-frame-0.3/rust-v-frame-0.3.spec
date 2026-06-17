# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name v_frame
%global full_version 0.3.9
%global pkgname v-frame-0.3

Name:           rust-v-frame-0.3
Version:        0.3.9
Release:        %autorelease
Summary:        Rust crate "v_frame"
License:        BSD-2-Clause
URL:            https://github.com/rust-av/v_frame
#!RemoteAsset:  sha256:666b7727c8875d6ab5db9533418d7c764233ac9c0cff1d469aec8fa127597be2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch0:          0001-fix-cargo-requirements.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(aligned-vec-0.6/default) >= 0.6.0
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(wasm-bindgen-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "v_frame"

%package     -n %{name}+profiling
Summary:        Video Frame data structures, originally part of rav1e - feature "profiling"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(profiling-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/profiling) = %{version}

%description -n %{name}+profiling
This metapackage enables feature "profiling" for the Rust v_frame crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Video Frame data structures, originally part of rav1e - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust v_frame crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Video Frame data structures, originally part of rav1e - feature "serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(aligned-vec-0.6/serde) >= 0.6.0
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
This metapackage enables feature "serialize" for the Rust v_frame crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Video Frame data structures, originally part of rav1e - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/profiling) = %{version}
Requires:       crate(profiling-1/profile-with-tracing) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.40
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust v_frame crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
