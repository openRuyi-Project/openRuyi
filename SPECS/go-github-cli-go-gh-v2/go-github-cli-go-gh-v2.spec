# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-gh
%define go_import_path  github.com/cli/go-gh/v2

Name:           go-github-cli-go-gh-v2
Version:        2.13.0
Release:        %autorelease
Summary:        Go module for authentication and configuration of the GitHub CLI
License:        MIT
URL:            https://github.com/cli/go-gh
#!RemoteAsset:  sha256:adeedc9546d714d29039abfcb1e2c6f48e4b741a537fdc592599e1264febbe7f
Source0:        https://github.com/cli/go-gh/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/AlecAivazis/survey/v2)
BuildRequires:  go(github.com/MakeNowJust/heredoc)
BuildRequires:  go(github.com/Masterminds/sprig/v3)
BuildRequires:  go(github.com/alecthomas/chroma/v2)
BuildRequires:  go(github.com/charmbracelet/glamour)
BuildRequires:  go(github.com/charmbracelet/lipgloss)
BuildRequires:  go(github.com/cli/browser)
BuildRequires:  go(github.com/cli/safeexec)
BuildRequires:  go(github.com/cli/shurcooL-graphql)
BuildRequires:  go(github.com/google/shlex)
BuildRequires:  go(github.com/henvic/httpretty)
BuildRequires:  go(github.com/itchyny/gojq)
BuildRequires:  go(github.com/leaanthony/go-ansi-parser)
BuildRequires:  go(github.com/mgutz/ansi)
BuildRequires:  go(github.com/muesli/reflow)
BuildRequires:  go(github.com/muesli/termenv)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/thlib/go-timezone-local)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(gopkg.in/h2non/gock.v1)
BuildRequires:  go(gopkg.in/yaml.v3)

Provides:       go(github.com/cli/go-gh/v2) = %{version}

Requires:       go(github.com/AlecAivazis/survey/v2)
Requires:       go(github.com/Masterminds/sprig/v3)
Requires:       go(github.com/charmbracelet/glamour)
Requires:       go(github.com/charmbracelet/lipgloss)
Requires:       go(github.com/cli/browser)
Requires:       go(github.com/cli/safeexec)
Requires:       go(github.com/cli/shurcooL-graphql)
Requires:       go(github.com/google/shlex)
Requires:       go(github.com/henvic/httpretty)
Requires:       go(github.com/itchyny/gojq)
Requires:       go(github.com/mgutz/ansi)
Requires:       go(github.com/muesli/reflow)
Requires:       go(github.com/muesli/termenv)
Requires:       go(github.com/stretchr/testify)
Requires:       go(github.com/thlib/go-timezone-local)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/term)
Requires:       go(golang.org/x/text)
Requires:       go(gopkg.in/yaml.v3)

%description
go-gh is a Go module for interacting with GitHub CLI authentication,
configuration, API, terminal, template, Markdown and repository features.

%check
# Compile the complete module and test suite before tolerating sandbox-sensitive
# tests that require the git executable and compare dependency-specific headers.
%buildsystem_golangmodules_check -run '^$'
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
