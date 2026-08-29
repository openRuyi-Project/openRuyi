# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pasetors
%global full_version 0.7.8
%global pkgname pasetors-0.7

Name:           rust-pasetors-0.7
Version:        0.7.8
Release:        %autorelease
Summary:        Rust crate "pasetors"
License:        MIT
URL:            https://github.com/brycx/pasetors
#!RemoteAsset:  sha256:e838401fb2873bad417e6a03179014c748746f67311cb7317ab14fc0881fa9f0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ct-codecs-1) >= 1.1.1
Requires:       crate(getrandom-0.4/default) >= 0.4.0
Requires:       crate(subtle-2) >= 2.4.1
Requires:       crate(zeroize-1) >= 1.4.1
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pasetors"

%package     -n %{name}+default
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/paserk) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/v4) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ed25519-compact
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "ed25519-compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ed25519-compact-2/random) >= 2.0.2
Provides:       crate(%{pkgname}/ed25519-compact) = %{version}

%description -n %{name}+ed25519-compact
This metapackage enables feature "ed25519-compact" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+orion
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "orion" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(orion-0.17) >= 0.17.0
Provides:       crate(%{pkgname}/orion) = %{version}
Provides:       crate(%{pkgname}/paserk) = %{version}

%description -n %{name}+orion
This metapackage enables feature "orion" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "paserk" feature.

%package     -n %{name}+p384
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "p384"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(p384-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/p384) = %{version}

%description -n %{name}+p384
This metapackage enables feature "p384" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand-core
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "rand_core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-core-0.6/getrandom) >= 0.6.3
Provides:       crate(%{pkgname}/rand-core) = %{version}

%description -n %{name}+rand-core
This metapackage enables feature "rand_core" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.5.5
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-derive-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-json
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "serde_json"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.41
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sha2
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "sha2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.10/default) >= 0.10.2
Provides:       crate(%{pkgname}/sha2) = %{version}

%description -n %{name}+sha2
This metapackage enables feature "sha2" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/serde-json) = %{version}
Requires:       crate(%{pkgname}/time) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+time
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "time"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(time-0.3/default) >= 0.3.0
Requires:       crate(time-0.3/formatting) >= 0.3.0
Requires:       crate(time-0.3/parsing) >= 0.3.0
Provides:       crate(%{pkgname}/time) = %{version}

%description -n %{name}+time
This metapackage enables feature "time" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "v2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/ed25519-compact) = %{version}
Requires:       crate(%{pkgname}/orion) = %{version}
Provides:       crate(%{pkgname}/v2) = %{version}
Provides:       crate(%{pkgname}/v4) = %{version}

%description -n %{name}+v2
This metapackage enables feature "v2" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "v4" feature.

%package     -n %{name}+v3
Summary:        PASETO: Platform-Agnostic Security Tokens (in Rust) - feature "v3"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/p384) = %{version}
Requires:       crate(%{pkgname}/rand-core) = %{version}
Requires:       crate(%{pkgname}/sha2) = %{version}
Provides:       crate(%{pkgname}/v3) = %{version}

%description -n %{name}+v3
This metapackage enables feature "v3" for the Rust pasetors crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
