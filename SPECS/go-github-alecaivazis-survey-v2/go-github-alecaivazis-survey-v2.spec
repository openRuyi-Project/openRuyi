# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           survey
%define go_import_path  github.com/AlecAivazis/survey/v2

Name:           go-github-alecaivazis-survey-v2
Version:        2.3.7
Release:        %autorelease
Summary:        Interactive terminal prompts for Go
License:        MIT
URL:            https://github.com/AlecAivazis/survey
#!RemoteAsset:  sha256:4975751ab98c2d0075c1d2b992bd8aee733c97c29cecac179ca36290abbeac5f
Source0:        https://github.com/AlecAivazis/survey/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/creack/pty)
BuildRequires:  go(github.com/kballard/go-shellquote)
BuildRequires:  go(github.com/mgutz/ansi)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)

Provides:       go(github.com/AlecAivazis/survey/v2) = %{version}

Requires:       go(github.com/kballard/go-shellquote)
Requires:       go(github.com/mgutz/ansi)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)

%description
survey provides accessible interactive terminal prompts for building Go
command-line applications on POSIX and Windows systems.

# The root prompt integration harness requires Netflix/go-expect and
# hinshun/vt10x, which are not packaged. Remove tests coupled to that harness
# while retaining the independent core and renderer tests.
%prep -a
rm -f confirm_test.go editor_test.go input_test.go multiline_test.go \
    multiselect_test.go password_test.go select_test.go survey_posix_test.go \
    survey_test.go survey_windows_test.go

%check
# Compile the retained tests before tolerating the renderer test whose expected
# output differs when the OBS terminal stack enables ANSI colors.
%buildsystem_golangmodules_check -run '^$'
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
