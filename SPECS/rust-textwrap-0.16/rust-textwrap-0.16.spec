# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name textwrap
%global full_version 0.16.2
%global pkgname textwrap-0.16

Name:           rust-textwrap-0.16
Version:        0.16.2
Release:        %autorelease
Summary:        Rust crate "textwrap"
License:        MIT
URL:            https://github.com/mgeisler/textwrap
#!RemoteAsset:  sha256:c13547615a44dc9c452a8a534638acdf07120d4b6847c8178705da06306a3057
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}

%description
Has optional support for Unicode and emojis as well as machine hyphenation.
Source code for takopackized Rust crate "textwrap"

%package     -n %{name}+default
Summary:        Word wrapping, indenting, and dedenting strings - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/smawk) = %{version}
Requires:       crate(%{pkgname}/unicode-linebreak) = %{version}
Requires:       crate(%{pkgname}/unicode-width) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "default" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hyphenation
Summary:        Word wrapping, indenting, and dedenting strings - feature "hyphenation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hyphenation-0.8/default) >= 0.8.4
Requires:       crate(hyphenation-0.8/embed-en-us) >= 0.8.4
Provides:       crate(%{pkgname}/hyphenation) = %{version}

%description -n %{name}+hyphenation
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "hyphenation" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smawk
Summary:        Word wrapping, indenting, and dedenting strings - feature "smawk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smawk-0.3/default) >= 0.3.2
Provides:       crate(%{pkgname}/smawk) = %{version}

%description -n %{name}+smawk
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "smawk" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+terminal-size
Summary:        Word wrapping, indenting, and dedenting strings - feature "terminal_size"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(terminal-size-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/terminal-size) = %{version}

%description -n %{name}+terminal-size
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "terminal_size" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-linebreak
Summary:        Word wrapping, indenting, and dedenting strings - feature "unicode-linebreak"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-linebreak-0.1/default) >= 0.1.5
Provides:       crate(%{pkgname}/unicode-linebreak) = %{version}

%description -n %{name}+unicode-linebreak
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "unicode-linebreak" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-width
Summary:        Word wrapping, indenting, and dedenting strings - feature "unicode-width"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/unicode-width) = %{version}

%description -n %{name}+unicode-width
Has optional support for Unicode and emojis as well as machine hyphenation.
This metapackage enables feature "unicode-width" for the Rust textwrap crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
