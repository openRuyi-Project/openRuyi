# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name insta
%global full_version 1.47.2
%global pkgname insta-1.0

Name:           rust-insta-1.0
Version:        1.47.2
Release:        %autorelease
Summary:        Rust crate "insta"
License:        Apache-2.0
URL:            https://insta.rs/
#!RemoteAsset:  sha256:7b4a6248eb93a4401ed2f37dfe8ea592d3cf05b7cf4f8efa867b6895af7e094e
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(similar-2.0/default) >= 2.7.0
Requires:       crate(similar-2.0/inline) >= 2.7.0
Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "insta"

%package     -n %{name}+clap
Summary:        Snapshot testing library for Rust - feature "clap" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(clap-4.0/default) >= 4.1
Requires:       crate(clap-4.0/derive) >= 4.1
Requires:       crate(clap-4.0/env) >= 4.1
Provides:       crate(%{pkgname}/cargo-insta-internal)
Provides:       crate(%{pkgname}/clap)

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "_cargo_insta_internal" feature.

%package     -n %{name}+console
Summary:        Snapshot testing library for Rust - feature "console" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(console-0.16/std) >= 0.16.1
Provides:       crate(%{pkgname}/colors)
Provides:       crate(%{pkgname}/console)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+console
This metapackage enables feature "console" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "colors", and "default" features.

%package     -n %{name}+csv
Summary:        Snapshot testing library for Rust - feature "csv"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(csv-1.0/default) >= 1.1.6
Provides:       crate(%{pkgname}/csv)

%description -n %{name}+csv
This metapackage enables feature "csv" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+glob
Summary:        Snapshot testing library for Rust - feature "glob"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/globset)
Requires:       crate(%{pkgname}/walkdir)
Provides:       crate(%{pkgname}/glob)

%description -n %{name}+glob
This metapackage enables feature "glob" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+globset
Summary:        Snapshot testing library for Rust - feature "globset"
Requires:       crate(%{pkgname})
Requires:       crate(globset-0.4/default) >= 0.4.6
Provides:       crate(%{pkgname}/globset)

%description -n %{name}+globset
This metapackage enables feature "globset" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest
Summary:        Snapshot testing library for Rust - feature "pest"
Requires:       crate(%{pkgname})
Requires:       crate(pest-2.0/default) >= 2.8.2
Provides:       crate(%{pkgname}/pest)

%description -n %{name}+pest
This metapackage enables feature "pest" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pest-derive
Summary:        Snapshot testing library for Rust - feature "pest_derive"
Requires:       crate(%{pkgname})
Requires:       crate(pest-derive-2.0/default) >= 2.8.2
Provides:       crate(%{pkgname}/pest-derive)

%description -n %{name}+pest-derive
This metapackage enables feature "pest_derive" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+redactions
Summary:        Snapshot testing library for Rust - feature "redactions"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pest)
Requires:       crate(%{pkgname}/pest-derive)
Requires:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/redactions)

%description -n %{name}+redactions
This metapackage enables feature "redactions" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Snapshot testing library for Rust - feature "regex" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/std) >= 1.12.3
Requires:       crate(regex-1.0/unicode) >= 1.12.3
Provides:       crate(%{pkgname}/filters)
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "filters" feature.

%package     -n %{name}+ron
Summary:        Snapshot testing library for Rust - feature "ron"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(ron-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}/ron)

%description -n %{name}+ron
This metapackage enables feature "ron" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Snapshot testing library for Rust - feature "serde" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/json)
Provides:       crate(%{pkgname}/serde)
Provides:       crate(%{pkgname}/yaml)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json", and "yaml" features.

%package     -n %{name}+toml
Summary:        Snapshot testing library for Rust - feature "toml"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/serde)
Requires:       crate(toml-edit-0.25/default) >= 0.25.0
Requires:       crate(toml-edit-0.25/display) >= 0.25.0
Requires:       crate(toml-edit-0.25/parse) >= 0.25.0
Requires:       crate(toml-edit-0.25/serde) >= 0.25.0
Requires:       crate(toml-writer-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/toml)

%description -n %{name}+toml
This metapackage enables feature "toml" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+walkdir
Summary:        Snapshot testing library for Rust - feature "walkdir"
Requires:       crate(%{pkgname})
Requires:       crate(walkdir-2.0/default) >= 2.3.1
Provides:       crate(%{pkgname}/walkdir)

%description -n %{name}+walkdir
This metapackage enables feature "walkdir" for the Rust insta crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
