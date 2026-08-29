# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inquire
%global full_version 0.9.2
%global pkgname inquire-0.9

Name:           rust-inquire-0.9
Version:        0.9.2
Release:        %autorelease
Summary:        Rust crate "inquire"
License:        MIT
URL:            https://github.com/mikaelmello/inquire
#!RemoteAsset:  sha256:ae51d5da01ce7039024fbdec477767c102c454dbdb09d4e2a432ece705b1b25d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(dyn-clone-1/default) >= 1.0.0
Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/macros) = %{version}
Provides:       crate(%{pkgname}/one-liners) = %{version}

%description
Source code for takopackized Rust crate "inquire"

%package     -n %{name}+chrono
Summary:        Building interactive prompts on terminals - feature "chrono" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(chrono-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/chrono) = %{version}
Provides:       crate(%{pkgname}/date) = %{version}

%description -n %{name}+chrono
This metapackage enables feature "chrono" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "date" feature.

%package     -n %{name}+console
Summary:        Building interactive prompts on terminals - feature "console"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(console-0.16/default) >= 0.16.0
Requires:       crate(console-0.16/windows-console-colors) >= 0.16.0
Provides:       crate(%{pkgname}/console) = %{version}

%description -n %{name}+console
This metapackage enables feature "console" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossterm
Summary:        Building interactive prompts on terminals - feature "crossterm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossterm-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/crossterm) = %{version}

%description -n %{name}+crossterm
This metapackage enables feature "crossterm" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Building interactive prompts on terminals - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crossterm) = %{version}
Requires:       crate(%{pkgname}/fuzzy) = %{version}
Requires:       crate(%{pkgname}/macros) = %{version}
Requires:       crate(%{pkgname}/one-liners) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fuzzy-matcher
Summary:        Building interactive prompts on terminals - feature "fuzzy-matcher" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fuzzy-matcher-0.3) >= 0.3.7
Provides:       crate(%{pkgname}/fuzzy) = %{version}
Provides:       crate(%{pkgname}/fuzzy-matcher) = %{version}

%description -n %{name}+fuzzy-matcher
This metapackage enables feature "fuzzy-matcher" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "fuzzy" feature.

%package     -n %{name}+tempfile
Summary:        Building interactive prompts on terminals - feature "tempfile" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}/editor) = %{version}
Provides:       crate(%{pkgname}/tempfile) = %{version}

%description -n %{name}+tempfile
This metapackage enables feature "tempfile" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "editor" feature.

%package     -n %{name}+termion
Summary:        Building interactive prompts on terminals - feature "termion"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termion-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/termion) = %{version}

%description -n %{name}+termion
This metapackage enables feature "termion" for the Rust inquire crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
