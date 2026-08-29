# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name schemars
%global full_version 0.8.22
%global pkgname schemars-0.8

Name:           rust-schemars-0.8
Version:        0.8.22
Release:        %autorelease
Summary:        Rust crate "schemars"
License:        MIT
URL:            https://graham.cool/schemars/
#!RemoteAsset:  sha256:3fbf2ae1b8bc8e02df939598064d22402220cd5bbcca1c76f7d6a310974d5615
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dyn-clone-1/default) >= 1.0.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.25
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/ui-test) = %{version}

%description
Source code for takopackized Rust crate "schemars"

%package     -n %{name}+arrayvec05
Summary:        Generate JSON Schemas from Rust code - feature "arrayvec05" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.5) >= 0.5.0
Provides:       crate(%{pkgname}/arrayvec) = %{version}
Provides:       crate(%{pkgname}/arrayvec05) = %{version}

%description -n %{name}+arrayvec05
This metapackage enables feature "arrayvec05" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "arrayvec" feature.

%package     -n %{name}+arrayvec07
Summary:        Generate JSON Schemas from Rust code - feature "arrayvec07"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(arrayvec-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/arrayvec07) = %{version}

%description -n %{name}+arrayvec07
This metapackage enables feature "arrayvec07" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bigdecimal03
Summary:        Generate JSON Schemas from Rust code - feature "bigdecimal03" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/bigdecimal) = %{version}
Provides:       crate(%{pkgname}/bigdecimal03) = %{version}

%description -n %{name}+bigdecimal03
This metapackage enables feature "bigdecimal03" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "bigdecimal" feature.

%package     -n %{name}+bigdecimal04
Summary:        Generate JSON Schemas from Rust code - feature "bigdecimal04"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bigdecimal-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/bigdecimal04) = %{version}

%description -n %{name}+bigdecimal04
This metapackage enables feature "bigdecimal04" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        Generate JSON Schemas from Rust code - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+chrono
Summary:        Generate JSON Schemas from Rust code - feature "chrono"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+either
Summary:        Generate JSON Schemas from Rust code - feature "either"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(either-1) >= 1.3.0
Provides:       crate(%{pkgname}/either) = %{version}

%description -n %{name}+either
This metapackage enables feature "either" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+enumset
Summary:        Generate JSON Schemas from Rust code - feature "enumset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(enumset-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/enumset) = %{version}

%description -n %{name}+enumset
This metapackage enables feature "enumset" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Generate JSON Schemas from Rust code - feature "indexmap" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-1/default) >= 1.2.0
Requires:       crate(indexmap-1/serde-1) >= 1.2.0
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/indexmap1) = %{version}
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "indexmap1", and "preserve_order" features.

%package     -n %{name}+indexmap2
Summary:        Generate JSON Schemas from Rust code - feature "indexmap2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Requires:       crate(indexmap-2/serde) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap2) = %{version}

%description -n %{name}+indexmap2
This metapackage enables feature "indexmap2" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+raw-value
Summary:        Generate JSON Schemas from Rust code - feature "raw_value"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/raw-value) >= 1.0.25
Provides:       crate(%{pkgname}/raw-value) = %{version}

%description -n %{name}+raw-value
This metapackage enables feature "raw_value" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-decimal
Summary:        Generate JSON Schemas from Rust code - feature "rust_decimal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-decimal-1) >= 1.0.0
Provides:       crate(%{pkgname}/rust-decimal) = %{version}

%description -n %{name}+rust-decimal
This metapackage enables feature "rust_decimal" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars-derive
Summary:        Generate JSON Schemas from Rust code - feature "schemars_derive" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-derive-0.8/default) >= 0.8.22
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/derive-json-schema) = %{version}
Provides:       crate(%{pkgname}/impl-json-schema) = %{version}
Provides:       crate(%{pkgname}/schemars-derive) = %{version}

%description -n %{name}+schemars-derive
This metapackage enables feature "schemars_derive" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", "derive", "derive_json_schema", and "impl_json_schema" features.

%package     -n %{name}+semver
Summary:        Generate JSON Schemas from Rust code - feature "semver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(semver-1/default) >= 1.0.9
Requires:       crate(semver-1/serde) >= 1.0.9
Provides:       crate(%{pkgname}/semver) = %{version}

%description -n %{name}+semver
This metapackage enables feature "semver" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smallvec
Summary:        Generate JSON Schemas from Rust code - feature "smallvec"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smallvec-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/smallvec) = %{version}

%description -n %{name}+smallvec
This metapackage enables feature "smallvec" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol-str
Summary:        Generate JSON Schemas from Rust code - feature "smol_str"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smol-str-0.1/default) >= 0.1.17
Provides:       crate(%{pkgname}/smol-str) = %{version}

%description -n %{name}+smol-str
This metapackage enables feature "smol_str" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+url
Summary:        Generate JSON Schemas from Rust code - feature "url"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(url-2) >= 2.0.0
Provides:       crate(%{pkgname}/url) = %{version}

%description -n %{name}+url
This metapackage enables feature "url" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uuid08
Summary:        Generate JSON Schemas from Rust code - feature "uuid08" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/uuid) = %{version}
Provides:       crate(%{pkgname}/uuid08) = %{version}

%description -n %{name}+uuid08
This metapackage enables feature "uuid08" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "uuid" feature.

%package     -n %{name}+uuid1
Summary:        Generate JSON Schemas from Rust code - feature "uuid1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uuid-1) >= 1.0.0
Provides:       crate(%{pkgname}/uuid1) = %{version}

%description -n %{name}+uuid1
This metapackage enables feature "uuid1" for the Rust schemars crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
