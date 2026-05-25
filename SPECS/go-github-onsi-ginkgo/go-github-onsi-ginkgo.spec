# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ginkgo
%define go_import_path  github.com/onsi/ginkgo

Name:           go-github-onsi-ginkgo
Version:        1.16.5
Release:        %autorelease
Summary:        Modern testing framework for Go
License:        MIT
URL:            https://github.com/onsi/ginkgo
#!RemoteAsset:  sha256:0380c81321b764b75e76a7aa8fc8ab1ab361232a88d5b6124ef8b9a9e75d5287
Source0:        https://github.com/onsi/ginkgo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n ginkgo-1.16.5
# Go 1.25 vet flags Ginkgo v1's printf-style stenographer helpers when they
# intentionally print preformatted strings; keep tests enabled but disable vet.
BuildOption(check):  -vet=off
# Integration tests build temporary suites with GOPROXY disabled in OBS and
# fail with "GOPROXY list is not the empty string, but contains no entries".
%define go_test_exclude_glob github.com/onsi/ginkgo/integration

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-task/slim-sprig)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/nxadm/tail)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/onsi/gomega/gbytes)
BuildRequires:  go(github.com/onsi/gomega/gexec)
BuildRequires:  go(github.com/onsi/gomega/ghttp)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/unix)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(golang.org/x/tools/go/ast/inspector)
BuildRequires:  go(golang.org/x/xerrors)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/tomb.v1)
BuildRequires:  go(gopkg.in/yaml.v2)

Provides:       go(github.com/onsi/ginkgo) = %{version}
Provides:       go(github.com/onsi/ginkgo/config) = %{version}
Provides:       go(github.com/onsi/ginkgo/extensions/globals) = %{version}
Provides:       go(github.com/onsi/ginkgo/extensions/table) = %{version}
Provides:       go(github.com/onsi/ginkgo/formatter) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/convert) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/interrupthandler) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/nodot) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/outline) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/testrunner) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/testsuite) = %{version}
Provides:       go(github.com/onsi/ginkgo/ginkgo/watch) = %{version}
Provides:       go(github.com/onsi/ginkgo/integration) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/codelocation) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/containernode) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/failer) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/global) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/leafnodes) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/remote) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/spec) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/spec_iterator) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/specrunner) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/suite) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/testingtproxy) = %{version}
Provides:       go(github.com/onsi/ginkgo/internal/writer) = %{version}
Provides:       go(github.com/onsi/ginkgo/reporters) = %{version}
Provides:       go(github.com/onsi/ginkgo/reporters/stenographer) = %{version}
Provides:       go(github.com/onsi/ginkgo/reporters/stenographer/support/go-colorable) = %{version}
Provides:       go(github.com/onsi/ginkgo/reporters/stenographer/support/go-isatty) = %{version}
Provides:       go(github.com/onsi/ginkgo/types) = %{version}

Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-task/slim-sprig)
Requires:       go(github.com/nxadm/tail)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/unix)
Requires:       go(golang.org/x/tools)
Requires:       go(golang.org/x/tools/go/ast/inspector)
Requires:       go(gopkg.in/tomb.v1)

%description
Ginkgo is a behavior-driven testing framework for Go.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
