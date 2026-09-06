# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           datadog-agent
%define go_import_path  github.com/DataDog/datadog-agent
%define commit          7c02565fb890b34e37ee3aadb9efa6d87fa8aa69
# The complete agent repository contains platform integrations not used as Go libraries.
%define go_test_include %{go_import_path}/pkg/util/option

Name:           go-github-datadog-datadog-agent
Version:        7.78.4+git20260817.7c02565
Release:        %autorelease
Summary:        Datadog Agent Go source modules
License:        Apache-2.0
URL:            https://github.com/DataDog/datadog-agent
#!RemoteAsset:  sha256:b2a6db773ac91a9d7a9ff0f3d1034bf44a1c20065a0615295e3706a3488f6556
Source0:        https://github.com/DataDog/datadog-agent/archive/%{commit}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules
BuildOption(prep):  -n %{_name}-%{commit}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/DataDog/agent-payload/v5)
BuildRequires:  go(github.com/DataDog/datadog-api-client-go/v2)
BuildRequires:  go(github.com/DataDog/go-sqllexer)
BuildRequires:  go(github.com/DataDog/go-tuf)
BuildRequires:  go(github.com/DataDog/sketches-go)
BuildRequires:  go(github.com/DataDog/viper)
BuildRequires:  go(github.com/benbjohnson/clock)
BuildRequires:  go(github.com/gofrs/flock)
BuildRequires:  go(github.com/mdlayher/vsock)
BuildRequires:  go(github.com/mohae/deepcopy)
BuildRequires:  go(github.com/outcaste-io/ristretto)
BuildRequires:  go(github.com/patrickmn/go-cache)
BuildRequires:  go(github.com/planetscale/vtprotobuf)
BuildRequires:  go(github.com/richardartoul/molecule)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/fx)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/DataDog/agent-payload/v5)
Requires:       go(github.com/DataDog/datadog-api-client-go/v2)
Requires:       go(github.com/DataDog/go-sqllexer)
Requires:       go(github.com/DataDog/go-tuf)
Requires:       go(github.com/DataDog/sketches-go)
Requires:       go(github.com/DataDog/viper)
Requires:       go(github.com/benbjohnson/clock)
Requires:       go(github.com/gofrs/flock)
Requires:       go(github.com/mdlayher/vsock)
Requires:       go(github.com/mohae/deepcopy)
Requires:       go(github.com/outcaste-io/ristretto)
Requires:       go(github.com/patrickmn/go-cache)
Requires:       go(github.com/planetscale/vtprotobuf)
Requires:       go(github.com/richardartoul/molecule)
Requires:       go(github.com/tinylib/msgp)
Requires:       go(go.uber.org/atomic)
Requires:       go(go.uber.org/fx)

%description
This source package installs the complete Datadog Agent repository, including
its component, telemetry mapping, protocol, trace, and utility Go modules.

%install -a
# Architecture-specific binaries are test fixtures, not Go source artifacts.
find "%{buildroot}%{go_sys_gopath}/%{go_import_path}" -type f \
    \( -name '*.so' -o -name '*.dll' -o -name '*.o' -o -name '*.exe' \) \
    -delete
rm -f "%{buildroot}%{go_sys_gopath}/%{go_import_path}"/pkg/network/usm/testdata/site-packages/ddtrace/libssl.so.*
find "%{buildroot}%{go_sys_gopath}/%{go_import_path}" -type f -exec chmod a-x {} +

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
