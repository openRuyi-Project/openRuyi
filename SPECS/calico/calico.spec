# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           calico
Version:        3.32.0
Release:        %autorelease
Summary:        Calico manifests for openRuyi RISC-V Kubernetes clusters
License:        Apache-2.0
URL:            https://github.com/projectcalico/calico
BuildArch:      noarch
#!RemoteAsset:  sha256:55defb4135a7f04942ff596848b4decc5eeed67d0d97f81b57df5395f41354c9
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Kubernetes multi-document manifests: upstream CRDs and the validated RISC-V deployment.
Source1:        calico-v%{version}-crds.yaml.in
Source2:        calico-v%{version}-openruyi-riscv64.yaml.in
Source3:        README.openruyi

Recommends:     kubernetes

%description
Calico provides Kubernetes pod networking and network policy. This package
installs the Calico v3.32.0 CRD manifest and the openRuyi RISC-V multi-node
VXLAN manifest used by the validated Kata Containers and Cloud Hypervisor
Kubernetes environment.

%prep
%setup -q -n %{name}-%{version}

%build
# Nothing to build; the package installs Kubernetes manifests.

%install
install -Dpm0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/kubernetes/calico/calico-v%{version}-crds.yaml
install -Dpm0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/kubernetes/calico/calico-v%{version}-openruyi-riscv64.yaml
install -Dpm0644 %{SOURCE3} \
    %{buildroot}%{_datadir}/kubernetes/calico/README.openruyi

%check
grep -q 'localhost/kubernetes/calico:v%{version}-riscv64' %{SOURCE2}
grep -q 'vxlanMode: Always' %{SOURCE2}
grep -q 'interface=eth1' %{SOURCE2}

%files
%doc README.md
%license LICENSE.md
%dir %{_datadir}/kubernetes
%dir %{_datadir}/kubernetes/calico
%{_datadir}/kubernetes/calico/calico-v%{version}-crds.yaml
%{_datadir}/kubernetes/calico/calico-v%{version}-openruyi-riscv64.yaml
%{_datadir}/kubernetes/calico/README.openruyi

%changelog
%autochangelog
