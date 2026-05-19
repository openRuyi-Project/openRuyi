# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name schemars
%global full_version 1.2.1
%global pkgname schemars-1.0

Name:           rust-schemars-1.0
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "schemars"
License:        MIT
URL:            https://graham.cool/schemars/
#!RemoteAsset:  sha256:a2b42f36aa1cd011945615b92222f6bf73c599a102a300334cd7f8dbeec726cc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dyn-clone-1.0/default) >= 1.0.20
Requires:       crate(ref-cast-1.0/default) >= 1.0.25
Requires:       crate(serde-1.0/alloc) >= 1.0.228
Requires:       crate(serde-json-1.0/alloc) >= 1.0.149
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/ui-test)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "schemars"

%package     -n %{name}+arrayvec07
Summary:        Generate JSON Schemas from Rust code - feature "arrayvec07"
Requires:       crate(%{pkgname})
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec07)

%description -n %{name}+arrayvec07
This metapackage enables feature "arrayvec07" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal04
Summary:        Generate JSON Schemas from Rust code - feature "bigdecimal04"
Requires:       crate(%{pkgname})
Requires:       crate(bigdecimal-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/bigdecimal04)

%description -n %{name}+bigdecimal04
This metapackage enables feature "bigdecimal04" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes1
Summary:        Generate JSON Schemas from Rust code - feature "bytes1"
Requires:       crate(%{pkgname})
Requires:       crate(bytes-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bytes1)

%description -n %{name}+bytes1
This metapackage enables feature "bytes1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono04
Summary:        Generate JSON Schemas from Rust code - feature "chrono04"
Requires:       crate(%{pkgname})
Requires:       crate(chrono-0.4) >= 0.4.39
Provides:       crate(%{pkgname}/chrono04)

%description -n %{name}+chrono04
This metapackage enables feature "chrono04" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Generate JSON Schemas from Rust code - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/derive)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either1
Summary:        Generate JSON Schemas from Rust code - feature "either1"
Requires:       crate(%{pkgname})
Requires:       crate(either-1.0) >= 1.3
Provides:       crate(%{pkgname}/either1)

%description -n %{name}+either1
This metapackage enables feature "either1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap2
Summary:        Generate JSON Schemas from Rust code - feature "indexmap2"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0) >= 2.2.3
Provides:       crate(%{pkgname}/indexmap2)

%description -n %{name}+indexmap2
This metapackage enables feature "indexmap2" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jiff02
Summary:        Generate JSON Schemas from Rust code - feature "jiff02"
Requires:       crate(%{pkgname})
Requires:       crate(jiff-0.2) >= 0.2.0
Provides:       crate(%{pkgname}/jiff02)

%description -n %{name}+jiff02
This metapackage enables feature "jiff02" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Generate JSON Schemas from Rust code - feature "preserve_order"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/alloc) >= 1.0.149
Requires:       crate(serde-json-1.0/preserve-order) >= 1.0.149
Provides:       crate(%{pkgname}/preserve-order)

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-value
Summary:        Generate JSON Schemas from Rust code - feature "raw_value"
Requires:       crate(%{pkgname})
Requires:       crate(serde-json-1.0/alloc) >= 1.0.149
Requires:       crate(serde-json-1.0/raw-value) >= 1.0.149
Provides:       crate(%{pkgname}/raw-value)

%description -n %{name}+raw-value
This metapackage enables feature "raw_value" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal1
Summary:        Generate JSON Schemas from Rust code - feature "rust_decimal1"
Requires:       crate(%{pkgname})
Requires:       crate(rust-decimal-1.0) >= 1.13
Provides:       crate(%{pkgname}/rust-decimal1)

%description -n %{name}+rust-decimal1
This metapackage enables feature "rust_decimal1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars-derive
Summary:        Generate JSON Schemas from Rust code - feature "schemars_derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(schemars-derive-1.0/default) >= 1.2.1
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/schemars-derive)

%description -n %{name}+schemars-derive
This metapackage enables feature "schemars_derive" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+semver1
Summary:        Generate JSON Schemas from Rust code - feature "semver1"
Requires:       crate(%{pkgname})
Requires:       crate(semver-1.0) >= 1.0.9
Provides:       crate(%{pkgname}/semver1)

%description -n %{name}+semver1
This metapackage enables feature "semver1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec1
Summary:        Generate JSON Schemas from Rust code - feature "smallvec1"
Requires:       crate(%{pkgname})
Requires:       crate(smallvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec1)

%description -n %{name}+smallvec1
This metapackage enables feature "smallvec1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str02
Summary:        Generate JSON Schemas from Rust code - feature "smol_str02"
Requires:       crate(%{pkgname})
Requires:       crate(smol-str-0.2) >= 0.2.1
Provides:       crate(%{pkgname}/smol-str02)

%description -n %{name}+smol-str02
This metapackage enables feature "smol_str02" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str03
Summary:        Generate JSON Schemas from Rust code - feature "smol_str03"
Requires:       crate(%{pkgname})
Requires:       crate(smol-str-0.3) >= 0.3.2
Provides:       crate(%{pkgname}/smol-str03)

%description -n %{name}+smol-str03
This metapackage enables feature "smol_str03" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url2
Summary:        Generate JSON Schemas from Rust code - feature "url2"
Requires:       crate(%{pkgname})
Requires:       crate(url-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/url2)

%description -n %{name}+url2
This metapackage enables feature "url2" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid1
Summary:        Generate JSON Schemas from Rust code - feature "uuid1"
Requires:       crate(%{pkgname})
Requires:       crate(uuid-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/uuid1)

%description -n %{name}+uuid1
This metapackage enables feature "uuid1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
