# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name criterion
%global full_version 0.7.0
%global pkgname criterion-0.7

Name:           rust-criterion-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "criterion"
License:        Apache-2.0 OR MIT
URL:            https://bheisler.github.io/criterion.rs/book/index.html
#!RemoteAsset:  sha256:e1c047a62b0cc3e145fa84415a3191f628e980b194c2755aa12300a4e6cbd928
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anes-0.1/default) >= 0.1.4
Requires:       crate(cast-0.3/default) >= 0.3.0
Requires:       crate(ciborium-0.2/default) >= 0.2.0
Requires:       crate(clap-4/help) >= 4.5.0
Requires:       crate(clap-4/std) >= 4.5.0
Requires:       crate(criterion-plot-0.6/default) >= 0.6.0
Requires:       crate(itertools-0.13/default) >= 0.13.0
Requires:       crate(num-traits-0.2/std) >= 0.2.0
Requires:       crate(oorandom-11/default) >= 11.1.0
Requires:       crate(regex-1/std) >= 1.5.1
Requires:       crate(serde-1/default) >= 1.0.100
Requires:       crate(serde-1/derive) >= 1.0.100
Requires:       crate(serde-json-1/default) >= 1.0.100
Requires:       crate(tinytemplate-1/default) >= 1.1.0
Requires:       crate(walkdir-2/default) >= 2.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/cargo-bench-support) = %{version}
Provides:       crate(%{pkgname}/html-reports) = %{version}
Provides:       crate(%{pkgname}/real-blackbox) = %{version}

%description
Source code for takopackized Rust crate "criterion"

%package     -n %{name}+async-futures
Summary:        Statistics-driven micro-benchmarking library - feature "async_futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/async-futures) = %{version}

%description -n %{name}+async-futures
This metapackage enables feature "async_futures" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-smol
Summary:        Statistics-driven micro-benchmarking library - feature "async_smol"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(smol-2) >= 2.0.0
Provides:       crate(%{pkgname}/async-smol) = %{version}

%description -n %{name}+async-smol
This metapackage enables feature "async_smol" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Statistics-driven micro-benchmarking library - feature "async_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(async-std-1/default) >= 1.13.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async_std" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio
Summary:        Statistics-driven micro-benchmarking library - feature "async_tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(tokio-1/rt) >= 1.0.0
Provides:       crate(%{pkgname}/async-tokio) = %{version}

%description -n %{name}+async-tokio
This metapackage enables feature "async_tokio" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+csv-output
Summary:        Statistics-driven micro-benchmarking library - feature "csv_output"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(csv-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/csv-output) = %{version}

%description -n %{name}+csv-output
This metapackage enables feature "csv_output" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Statistics-driven micro-benchmarking library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cargo-bench-support) = %{version}
Requires:       crate(%{pkgname}/plotters) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+plotters
Summary:        Statistics-driven micro-benchmarking library - feature "plotters"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(plotters-0.3/area-series) >= 0.3.2
Requires:       crate(plotters-0.3/line-series) >= 0.3.2
Requires:       crate(plotters-0.3/svg-backend) >= 0.3.2
Provides:       crate(%{pkgname}/plotters) = %{version}

%description -n %{name}+plotters
This metapackage enables feature "plotters" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Statistics-driven micro-benchmarking library - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rayon-1/default) >= 1.3.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+stable
Summary:        Statistics-driven micro-benchmarking library - feature "stable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-futures) = %{version}
Requires:       crate(%{pkgname}/async-smol) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Requires:       crate(%{pkgname}/async-tokio) = %{version}
Requires:       crate(%{pkgname}/csv-output) = %{version}
Requires:       crate(%{pkgname}/html-reports) = %{version}
Provides:       crate(%{pkgname}/stable) = %{version}

%description -n %{name}+stable
This metapackage enables feature "stable" for the Rust criterion crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
