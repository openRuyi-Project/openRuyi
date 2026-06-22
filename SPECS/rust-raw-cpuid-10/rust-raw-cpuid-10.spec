# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name raw-cpuid
%global full_version 10.7.0
%global pkgname raw-cpuid-10

Name:           rust-raw-cpuid-10
Version:        10.7.0
Release:        %autorelease
Summary:        Rust crate "raw-cpuid"
License:        MIT
URL:            https://github.com/gz/rust-cpuid
#!RemoteAsset:  sha256:6c297679cb867470fa8c9f67dbba74a78d78e3e98d7cf2b08d6d71540f797332
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
Source code for takopackized Rust crate "raw-cpuid"

%package     -n %{name}+clap
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-3/default) >= 3.1.6
Requires:       crate(clap-3/derive) >= 3.1.6
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "clap" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cli
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/display) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "cli" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "display"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/serialize) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/termimad) = %{version}
Provides:       crate(%{pkgname}/display) = %{version}

%description -n %{name}+display
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "display" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "serde" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-derive
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "serde_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-derive) = %{version}

%description -n %{name}+serde-derive
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "serde_derive" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "serde_json" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serialize
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "serialize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/serde-derive) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serialize
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "serialize" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+termimad
Summary:        Parse the x86 CPUID instruction, written in rust with no external dependencies - feature "termimad"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termimad-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/termimad) = %{version}

%description -n %{name}+termimad
The implementation closely resembles the Intel CPUID manual description. The library does only depend on libcore.
This metapackage enables feature "termimad" for the Rust raw-cpuid crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
