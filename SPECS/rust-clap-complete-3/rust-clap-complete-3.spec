# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name clap_complete
%global full_version 3.2.5
%global pkgname clap-complete-3

Name:           rust-clap-complete-3
Version:        3.2.5
Release:        %autorelease
Summary:        Rust crate "clap_complete"
License:        MIT OR Apache-2.0
URL:            https://github.com/clap-rs/clap/tree/master/clap_complete
#!RemoteAsset:  sha256:3f7a2e0a962c45ce25afce14220bc24f9dade0a1787f185cecf96bfba7847cd8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(clap-3/std) >= 3.2.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "clap_complete"

%package     -n %{name}+clap-lex
Summary:        Generate shell completion scripts for your clap::Command - feature "clap_lex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-lex-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/clap-lex) = %{version}

%description -n %{name}+clap-lex
This metapackage enables feature "clap_lex" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Generate shell completion scripts for your clap::Command - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-3/debug) >= 3.2.1
Requires:       crate(clap-3/std) >= 3.2.1
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-executable
Summary:        Generate shell completion scripts for your clap::Command - feature "is_executable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(is-executable-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/is-executable) = %{version}

%description -n %{name}+is-executable
This metapackage enables feature "is_executable" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+os-str-bytes
Summary:        Generate shell completion scripts for your clap::Command - feature "os_str_bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(os-str-bytes-6/raw-os-str) >= 6.0.0
Provides:       crate(%{pkgname}/os-str-bytes) = %{version}

%description -n %{name}+os-str-bytes
This metapackage enables feature "os_str_bytes" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pathdiff
Summary:        Generate shell completion scripts for your clap::Command - feature "pathdiff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pathdiff-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/pathdiff) = %{version}

%description -n %{name}+pathdiff
This metapackage enables feature "pathdiff" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+shlex
Summary:        Generate shell completion scripts for your clap::Command - feature "shlex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(shlex-1/default) >= 1.1.0
Provides:       crate(%{pkgname}/shlex) = %{version}

%description -n %{name}+shlex
This metapackage enables feature "shlex" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-xid
Summary:        Generate shell completion scripts for your clap::Command - feature "unicode-xid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-xid-0.2/default) >= 0.2.2
Provides:       crate(%{pkgname}/unicode-xid) = %{version}

%description -n %{name}+unicode-xid
This metapackage enables feature "unicode-xid" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-dynamic
Summary:        Generate shell completion scripts for your clap::Command - feature "unstable-dynamic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap-lex) = %{version}
Requires:       crate(%{pkgname}/is-executable) = %{version}
Requires:       crate(%{pkgname}/os-str-bytes) = %{version}
Requires:       crate(%{pkgname}/pathdiff) = %{version}
Requires:       crate(%{pkgname}/shlex) = %{version}
Requires:       crate(%{pkgname}/unicode-xid) = %{version}
Requires:       crate(clap-3/derive) >= 3.2.1
Requires:       crate(clap-3/std) >= 3.2.1
Provides:       crate(%{pkgname}/unstable-dynamic) = %{version}

%description -n %{name}+unstable-dynamic
This metapackage enables feature "unstable-dynamic" for the Rust clap_complete crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
