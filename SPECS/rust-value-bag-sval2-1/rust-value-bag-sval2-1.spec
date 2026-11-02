# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name value-bag-sval2
%global full_version 1.12.0
%global pkgname value-bag-sval2-1

Name:           rust-value-bag-sval2-1
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "value-bag-sval2"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/value-bag
#!RemoteAsset:  sha256:d00ae130edd690eaa877e4f40605d534790d1cf1d651e7685bd6a144521b251f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(sval-2) >= 2.1.0
Requires:       crate(sval-buffer-2) >= 2.3.0
Requires:       crate(sval-dynamic-2) >= 2.1.0
Requires:       crate(sval-fmt-2) >= 2.1.0
Requires:       crate(sval-ref-2) >= 2.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "value-bag-sval2"

%package     -n %{name}+alloc
Summary:        Implementation detail for value-bag - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2/alloc) >= 2.1.0
Requires:       crate(sval-buffer-2/alloc) >= 2.3.0
Requires:       crate(sval-json-2/alloc) >= 2.1.0
Requires:       crate(sval-ref-2/alloc) >= 2.1.0
Requires:       crate(sval-serde-2/alloc) >= 2.1.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Implementation detail for value-bag - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-2/std) >= 2.1.0
Requires:       crate(sval-buffer-2/std) >= 2.3.0
Requires:       crate(sval-json-2/std) >= 2.1.0
Requires:       crate(sval-ref-2/std) >= 2.1.0
Requires:       crate(sval-serde-2/std) >= 2.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sval-json
Summary:        Implementation detail for value-bag - feature "sval_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-json-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/sval-json) = %{version}

%description -n %{name}+sval-json
This metapackage enables feature "sval_json" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+sval-serde
Summary:        Implementation detail for value-bag - feature "sval_serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-serde-2) >= 2.1.0
Provides:       crate(%{pkgname}/serde1) = %{version}
Provides:       crate(%{pkgname}/sval-serde) = %{version}

%description -n %{name}+sval-serde
This metapackage enables feature "sval_serde" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde1" feature.

%package     -n %{name}+sval-test
Summary:        Implementation detail for value-bag - feature "sval_test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sval-test-2/default) >= 2.1.0
Provides:       crate(%{pkgname}/sval-test) = %{version}

%description -n %{name}+sval-test
This metapackage enables feature "sval_test" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test
Summary:        Implementation detail for value-bag - feature "test"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/sval-test) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+test
This metapackage enables feature "test" for the Rust value-bag-sval2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
