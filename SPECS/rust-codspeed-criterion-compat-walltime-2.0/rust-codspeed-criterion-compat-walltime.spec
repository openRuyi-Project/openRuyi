# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed-criterion-compat-walltime
%global full_version 2.10.1
%global pkgname codspeed-criterion-compat-walltime-2.0

Name:           rust-codspeed-criterion-compat-walltime-2.0
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "codspeed-criterion-compat-walltime"
License:        Apache-2.0 OR MIT
URL:            https://bheisler.github.io/criterion.rs/book/index.html
#!RemoteAsset:  sha256:7b0a2f7365e347f4f22a67e9ea689bf7bc89900a354e22e26cf8a531a42c8fbb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anes-0.1/default) >= 0.1.6
Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(ciborium-0.2/default) >= 0.2.2
Requires:       crate(clap-4.0/std) >= 4.6.1
Requires:       crate(codspeed-2.0/default) >= 2.10.1
Requires:       crate(criterion-plot-0.5/default) >= 0.5.0
Requires:       crate(is-terminal-0.4/default) >= 0.4.17
Requires:       crate(itertools-0.10/default) >= 0.10.5
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(oorandom-11.0/default) >= 11.1.5
Requires:       crate(regex-1.0/std) >= 1.12.3
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-derive-1.0/default) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(tinytemplate-1.0/default) >= 1.2.1
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cargo-bench-support)
Provides:       crate(%{pkgname}/html-reports)
Provides:       crate(%{pkgname}/real-blackbox)

%description
Source code for takopackized Rust crate "codspeed-criterion-compat-walltime"

%package     -n %{name}+async-futures
Summary:        Statistics-driven micro-benchmarking library - feature "async_futures"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/async-futures)

%description -n %{name}+async-futures
This metapackage enables feature "async_futures" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-smol
Summary:        Statistics-driven micro-benchmarking library - feature "async_smol"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/smol)
Provides:       crate(%{pkgname}/async-smol)

%description -n %{name}+async-smol
This metapackage enables feature "async_smol" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Statistics-driven micro-benchmarking library - feature "async_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(async-std-1.0/default) >= 1.9
Provides:       crate(%{pkgname}/async-std)

%description -n %{name}+async-std
This metapackage enables feature "async_std" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio
Summary:        Statistics-driven micro-benchmarking library - feature "async_tokio"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/tokio)
Provides:       crate(%{pkgname}/async-tokio)

%description -n %{name}+async-tokio
This metapackage enables feature "async_tokio" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv
Summary:        Statistics-driven micro-benchmarking library - feature "csv" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(csv-1.0/default) >= 1.1
Provides:       crate(%{pkgname}/csv)
Provides:       crate(%{pkgname}/csv-output)

%description -n %{name}+csv
This metapackage enables feature "csv" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "csv_output" feature.

%package     -n %{name}+default
Summary:        Statistics-driven micro-benchmarking library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cargo-bench-support)
Requires:       crate(%{pkgname}/plotters)
Requires:       crate(%{pkgname}/rayon)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Statistics-driven micro-benchmarking library - feature "futures" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/async)
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%package     -n %{name}+plotters
Summary:        Statistics-driven micro-benchmarking library - feature "plotters"
Requires:       crate(%{pkgname})
Requires:       crate(plotters-0.3/area-series) >= 0.3.7
Requires:       crate(plotters-0.3/line-series) >= 0.3.7
Requires:       crate(plotters-0.3/svg-backend) >= 0.3.7
Provides:       crate(%{pkgname}/plotters)

%description -n %{name}+plotters
This metapackage enables feature "plotters" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Statistics-driven micro-benchmarking library - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(rayon-1.0/default) >= 1.12.0
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        Statistics-driven micro-benchmarking library - feature "smol"
Requires:       crate(%{pkgname})
Requires:       crate(smol-1.0) >= 1.2
Provides:       crate(%{pkgname}/smol)

%description -n %{name}+smol
This metapackage enables feature "smol" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable
Summary:        Statistics-driven micro-benchmarking library - feature "stable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-futures)
Requires:       crate(%{pkgname}/async-smol)
Requires:       crate(%{pkgname}/async-std)
Requires:       crate(%{pkgname}/async-tokio)
Requires:       crate(%{pkgname}/csv-output)
Requires:       crate(%{pkgname}/html-reports)
Provides:       crate(%{pkgname}/stable)

%description -n %{name}+stable
This metapackage enables feature "stable" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Statistics-driven micro-benchmarking library - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/rt) >= 1.0.0
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust codspeed-criterion-compat-walltime crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
