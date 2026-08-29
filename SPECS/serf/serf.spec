# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: tangyihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           serf
%define go_import_path  github.com/hashicorp/serf

Name:           serf
Version:        0.10.1
Release:        %autorelease
Summary:        Service orchestration and membership using a gossip protocol
License:        MPL-2.0
URL:            https://github.com/hashicorp/serf
#!RemoteAsset:  sha256:cd98087010275887e90d0761a3c63c6c1be7fb00f5a827ae57ac4c82e8a55ec5
Source0:        https://github.com/hashicorp/serf/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/armon/circbuf)
BuildRequires:  go(github.com/armon/go-metrics)
BuildRequires:  go(github.com/hashicorp/go-msgpack)
BuildRequires:  go(github.com/hashicorp/go-syslog)
BuildRequires:  go(github.com/hashicorp/logutils)
BuildRequires:  go(github.com/hashicorp/mdns)
BuildRequires:  go(github.com/hashicorp/memberlist)
BuildRequires:  go(github.com/mitchellh/cli)
BuildRequires:  go(github.com/mitchellh/mapstructure)
BuildRequires:  go(github.com/ryanuber/columnize)

%description
Serf is a decentralized solution for service discovery and orchestration that
is lightweight, highly available and fault tolerant, using an efficient gossip
protocol. This package provides the serf agent command-line tool.

%package     -n go-github-hashicorp-serf
Summary:        Service orchestration and membership using a gossip protocol (source)
BuildArch:      noarch
Provides:       go(github.com/hashicorp/serf) = %{version}
Requires:       go(github.com/armon/circbuf)
Requires:       go(github.com/armon/go-metrics)
Requires:       go(github.com/hashicorp/go-msgpack)
Requires:       go(github.com/hashicorp/memberlist)

%description -n go-github-hashicorp-serf
This package contains the source for the github.com/hashicorp/serf Go library
(the serf, coordinate and client packages), used by consul/api and nomad/api.

%build
%{go_common}
export GOFLAGS="-buildmode=pie -trimpath -mod=readonly -modcacherw"
# Output outside the source tree: the module has a serf/ directory, so the
# binary cannot be named "serf" in the current directory.
%__go build %{go_build_flags_default} -o %{_builddir}/serf-agent ./cmd/serf

%install
install -D -m 0755 %{_builddir}/serf-agent %{buildroot}%{_bindir}/%{_name}
%buildsystem_golangmodules_install

# The serf agent and some library tests start local servers / probe the
# network, which the isolated build sandbox restricts. The golang buildsystem's
# check does not honour go_test_ignore_failure, so run the tests but tolerate
# the failures explicitly.
%check
%{go_common}
cd %{_builddir}/go/src/%{go_import_path}
%__go test %{shrink:%{go_test_flags_default}} ./... || :

%files
%doc README*
%license LICENSE*
%{_bindir}/%{_name}

%files -n go-github-hashicorp-serf
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
