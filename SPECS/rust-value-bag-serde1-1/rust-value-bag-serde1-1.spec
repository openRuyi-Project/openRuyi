# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name value-bag-serde1
%global full_version 1.12.0
%global pkgname value-bag-serde1-1

Name:           rust-value-bag-serde1-1
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "value-bag-serde1"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/value-bag
#!RemoteAsset:  sha256:16530907bfe2999a1773ca5900a65101e092c70f642f25cc23ca0c43573262c5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(erased-serde-0.4/alloc) >= 0.4.9
Requires:       crate(serde-core-1/alloc) >= 1.0.0
Requires:       crate(serde-fmt-1) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "value-bag-serde1"

%package     -n %{name}+serde-buf
Summary:        Implementation detail for value-bag - feature "serde_buf" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-buf-0.1) >= 0.1.0
Provides:       crate(%{pkgname}/owned) = %{version}
Provides:       crate(%{pkgname}/serde-buf) = %{version}

%description -n %{name}+serde-buf
This metapackage enables feature "serde_buf" for the Rust value-bag-serde1 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "owned" feature.

%package     -n %{name}+serde-json
Summary:        Implementation detail for value-bag - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust value-bag-serde1 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+serde-test
Summary:        Implementation detail for value-bag - feature "serde_test" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-test-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-test) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+serde-test
This metapackage enables feature "serde_test" for the Rust value-bag-serde1 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "test" feature.

%package     -n %{name}+std
Summary:        Implementation detail for value-bag - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(erased-serde-0.4/alloc) >= 0.4.9
Requires:       crate(erased-serde-0.4/std) >= 0.4.9
Requires:       crate(serde-core-1/alloc) >= 1.0.0
Requires:       crate(serde-core-1/std) >= 1.0.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust value-bag-serde1 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
