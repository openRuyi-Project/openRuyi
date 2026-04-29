# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name codspeed-criterion-compat
%global full_version 2.10.1
%global pkgname codspeed-criterion-compat-2.0

Name:           rust-codspeed-criterion-compat-2.0
Version:        2.10.1
Release:        %autorelease
Summary:        Rust crate "codspeed-criterion-compat"
License:        MIT OR Apache-2.0
URL:            https://codspeed.io
#!RemoteAsset:  sha256:c3c23d880a28a2aab52d38ca8481dd7a3187157d0a952196b6db1db3c8499725
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(codspeed-2.0/default) >= 2.10.1
Requires:       crate(codspeed-criterion-compat-walltime-2.0) >= 2.10.1
Requires:       crate(colored-2.0/default) >= 2.2.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "codspeed-criterion-compat"

%package     -n %{name}+async
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures)
Requires:       crate(codspeed-criterion-compat-walltime-2.0/async) >= 2.10.1
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-futures
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_futures"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(codspeed-criterion-compat-walltime-2.0/async-futures) >= 2.10.1
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/async-futures)

%description -n %{name}+async-futures
This metapackage enables feature "async_futures" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-smol
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_smol"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/smol)
Requires:       crate(codspeed-criterion-compat-walltime-2.0/async-smol) >= 2.10.1
Provides:       crate(%{pkgname}/async-smol)

%description -n %{name}+async-smol
This metapackage enables feature "async_smol" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(async-std-1.0/default) >= 1.12
Requires:       crate(codspeed-criterion-compat-walltime-2.0/async-std) >= 2.10.1
Provides:       crate(%{pkgname}/async-std)

%description -n %{name}+async-std
This metapackage enables feature "async_std" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "async_tokio"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(codspeed-criterion-compat-walltime-2.0/async-tokio) >= 2.10.1
Provides:       crate(%{pkgname}/async-tokio)

%description -n %{name}+async-tokio
This metapackage enables feature "async_tokio" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cargo-bench-support
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "cargo_bench_support"
Requires:       crate(%{pkgname})
Requires:       crate(codspeed-criterion-compat-walltime-2.0/cargo-bench-support) >= 2.10.1
Provides:       crate(%{pkgname}/cargo-bench-support)

%description -n %{name}+cargo-bench-support
This metapackage enables feature "cargo_bench_support" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv-output
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "csv_output"
Requires:       crate(%{pkgname})
Requires:       crate(codspeed-criterion-compat-walltime-2.0/csv-output) >= 2.10.1
Provides:       crate(%{pkgname}/csv-output)

%description -n %{name}+csv-output
This metapackage enables feature "csv_output" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cargo-bench-support)
Requires:       crate(%{pkgname}/plotters)
Requires:       crate(%{pkgname}/rayon)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+html-reports
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "html_reports"
Requires:       crate(%{pkgname})
Requires:       crate(codspeed-criterion-compat-walltime-2.0/html-reports) >= 2.10.1
Provides:       crate(%{pkgname}/html-reports)

%description -n %{name}+html-reports
This metapackage enables feature "html_reports" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "plotters"
Requires:       crate(%{pkgname})
Requires:       crate(codspeed-criterion-compat-walltime-2.0/plotters) >= 2.10.1
Provides:       crate(%{pkgname}/plotters)

%description -n %{name}+plotters
This metapackage enables feature "plotters" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "rayon"
Requires:       crate(%{pkgname})
Requires:       crate(codspeed-criterion-compat-walltime-2.0/rayon) >= 2.10.1
Provides:       crate(%{pkgname}/rayon)

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smol
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "smol"
Requires:       crate(%{pkgname})
Requires:       crate(smol-2.0) >= 2.0.0
Provides:       crate(%{pkgname}/smol)

%description -n %{name}+smol
This metapackage enables feature "smol" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Criterion.rs compatibility layer for CodSpeed - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(tokio-1.0/rt) >= 1.39
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust codspeed-criterion-compat crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
