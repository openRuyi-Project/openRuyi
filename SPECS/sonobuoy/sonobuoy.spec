# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           sonobuoy
Version:        0.57.3
Release:        %autorelease
Summary:        Kubernetes cluster conformance and diagnostics tool
License:        Apache-2.0
URL:            https://github.com/vmware-tanzu/sonobuoy
#!RemoteAsset:  sha256:d581032898c17f1df6db90e85aae8dae6429e8cd2a1b54e1728ddeaa7d9a989c
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:a4e1f88aed223e6c52344b708a467ec83ea8783a8532b66bb0c28f5e6024cc93
Source1:        https://github.com/software-vendor/go-sonobuoy-vendor/releases/download/v%{version}/%{name}-%{version}-vendor.tar.gz
# RISC-V smoke-test manifest installed with the package.
Source2:        openruyi-riscv-sonobuoy-smoke.yaml

# Adapt the upstream IPv4 aggregator address fix for v%{version}.
# https://github.com/vmware-tanzu/sonobuoy/commit/08e4ff4475e5e30c596dc6f8ff94708b3750f9d4
Patch0:         0001-config-format-advertise-ip-with-net.JoinHostPort.patch

BuildRequires:  go >= 1.23
BuildRequires:  go-rpm-macros

Recommends:     kubernetes

%description
Sonobuoy is a diagnostic tool that makes it easier to understand the state of a
Kubernetes cluster by running plugins, collecting results, and producing a
portable result bundle.

%prep
%autosetup -n %{name}-%{version} -p1
tar -xzf %{SOURCE1}

%build
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-mod=vendor -trimpath -modcacherw"
export GOTOOLCHAIN=local

%__go build %{go_build_flags_default} -o %{name} .

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/openruyi-riscv-sonobuoy-smoke.yaml

%check
%{buildroot}%{_bindir}/%{name} version
%{buildroot}%{_bindir}/%{name} gen plugin --help >/dev/null

%files
%doc README.md CONTRIBUTING.md SECURITY.md vendor/modules.txt
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/openruyi-riscv-sonobuoy-smoke.yaml

%changelog
%autochangelog
