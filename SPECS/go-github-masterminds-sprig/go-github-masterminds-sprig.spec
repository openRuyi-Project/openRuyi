# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           sprig
%define go_import_path  github.com/Masterminds/sprig

Name:           go-github-masterminds-sprig
Version:        2.22.0
Release:        %autorelease
Summary:        Template functions for Go
License:        MIT
URL:            https://github.com/Masterminds/sprig
#!RemoteAsset:  sha256:c6d0f6e2a3b2aecc888b62c15defcccf16a44e7435c47c7f158b98946c5ee970
Source0:        https://github.com/Masterminds/sprig/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# https://github.com/Masterminds/sprig/commit/fe8e5b963cddb929b1ba4a9684401a84f382845a
Patch1000:      1000-Preserve-upper-camelcase-with-xstrings-1.5.patch
# Round the scaled value before Modf; fused arithmetic otherwise changes half-way results.
Patch2000:      2000-Prevent-fused-arithmetic-from-changing-round-results.patch

# The DNS lookup test requires network access.
BuildOption(check):  -skip '^TestGetHostByName$'

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/goutils)
BuildRequires:  go(github.com/Masterminds/semver)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/huandu/xstrings)
BuildRequires:  go(github.com/imdario/mergo)
BuildRequires:  go(github.com/mitchellh/copystructure)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)

Provides:       go(github.com/Masterminds/sprig) = %{version}

Requires:       go(github.com/Masterminds/goutils)
Requires:       go(github.com/Masterminds/semver)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/huandu/xstrings)
Requires:       go(github.com/imdario/mergo)
Requires:       go(github.com/mitchellh/copystructure)
Requires:       go(golang.org/x/crypto)

%description
Template functions for Go.

%check -p
# The legacy shuffle test expects the old deterministic math/rand default seed.
export GODEBUG=randautoseed=0

%files
%doc README.md
%license LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
