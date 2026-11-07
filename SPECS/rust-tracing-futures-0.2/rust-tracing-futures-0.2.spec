# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tracing-futures
%global full_version 0.2.5
%global pkgname tracing-futures-0.2

Name:           rust-tracing-futures-0.2
Version:        0.2.5
Release:        %autorelease
Summary:        Rust crate "tracing-futures"
License:        MIT
URL:            https://tokio.rs
#!RemoteAsset:  sha256:97d095ae15e245a057c8e8451bab9b3ee1e1f68e9ba2b4fbc18d0ac5237835f2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tracing-0.1) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tracing-futures"

%package     -n %{name}+default
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/std-future) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "futures"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-03
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "futures-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures) = %{version}
Requires:       crate(%{pkgname}/futures-task) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/std-future) = %{version}
Provides:       crate(%{pkgname}/futures-03) = %{version}

%description -n %{name}+futures-03
This metapackage enables feature "futures-03" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-task
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "futures-task"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-task-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-task) = %{version}

%description -n %{name}+futures-task
This metapackage enables feature "futures-task" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-01
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "futures_01"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(futures-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/futures-01) = %{version}

%description -n %{name}+futures-01
This metapackage enables feature "futures_01" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "pin-project" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/pin-project) = %{version}
Provides:       crate(%{pkgname}/std-future) = %{version}

%description -n %{name}+pin-project
This metapackage enables feature "pin-project" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "std-future" feature.

%package     -n %{name}+std
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.0
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-executor
Summary:        Utilities for instrumenting `futures` with `tracing` - feature "tokio-executor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-executor-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/tokio-executor) = %{version}

%description -n %{name}+tokio-executor
This metapackage enables feature "tokio-executor" for the Rust tracing-futures crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
