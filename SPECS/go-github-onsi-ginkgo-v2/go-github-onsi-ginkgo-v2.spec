# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ginkgo
%define go_import_path  github.com/onsi/ginkgo/v2
%define commit_id 4f62d7a74752034222d97d911f904d9be47ff7aa
# Integration tests run ginkgo watch and nested module commands. In OBS they
# timed out after 30s waiting for watched suites and failed module commands with
# "GOPROXY list is not the empty string, but contains no entries".
# - HNO3Miracle
%define go_test_exclude %{go_import_path}/integration

Name:           go-github-onsi-ginkgo-v2
Version:        0+git20260607.4f62d7a
Release:        %autorelease
Summary:        Behavior-driven testing framework for Go
License:        MIT
URL:            https://github.com/onsi/ginkgo
#!RemoteAsset:  sha256:0091ba7240d1e23e5086233c13044180a11351105cfce4b2f49149da55547067
Source0:        https://github.com/onsi/ginkgo/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Packaged Masterminds/semver quotes invalid constraint strings in error
# messages, unlike the version expected by this upstream snapshot. - HNO3Miracle
Patch2000:      2000-accept-quoted-semver-constraint-errors.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/Masterminds/semver/v3)
BuildRequires:  go(github.com/gkampitakis/ciinfo)
BuildRequires:  go(github.com/gkampitakis/go-diff)
BuildRequires:  go(github.com/gkampitakis/go-snaps)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-task/slim-sprig/v3)
BuildRequires:  go(github.com/goccy/go-yaml)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/pprof)
BuildRequires:  go(github.com/joshdk/go-junit)
BuildRequires:  go(github.com/kr/pretty)
BuildRequires:  go(github.com/kr/text)
BuildRequires:  go(github.com/maruel/natural)
BuildRequires:  go(github.com/mfridman/tparse)
BuildRequires:  go(github.com/onsi/gomega)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/tidwall/gjson)
BuildRequires:  go(github.com/tidwall/match)
BuildRequires:  go(github.com/tidwall/pretty)
BuildRequires:  go(github.com/tidwall/sjson)
BuildRequires:  go(go.yaml.in/yaml/v3)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(golang.org/x/tools)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/check.v1)

Provides:       go(github.com/onsi/ginkgo/v2) = %{version}

Requires:       go(github.com/Masterminds/semver/v3)
Requires:       go(github.com/go-logr/logr)
Requires:       go(github.com/go-task/slim-sprig/v3)
Requires:       go(github.com/google/pprof)
Requires:       go(github.com/onsi/gomega)
Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/tools)

%description
Ginkgo v2 is a behavior-driven testing framework for Go.

%files
%doc README.md
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
