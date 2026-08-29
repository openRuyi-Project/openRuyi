# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define git_commit      6636cbce3bbef91ff61d36658757179426f9e1b2

Name:           kubernetes
Version:        1.35.5
Release:        %autorelease
Summary:        Production-grade container orchestration system
License:        Apache-2.0
URL:            https://github.com/kubernetes/kubernetes
#!RemoteAsset:  sha256:c058972b598acb8fe08bc23e630e7e7582d86050bc78468c3026396a53ebc64b
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        kubelet.service
Source2:        10-kubeadm.conf
Source3:        kubelet.sysconfig

BuildRequires:  go >= 1.25.9
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Recommends:     containerd
Recommends:     conntrack-tools
Recommends:     cri-tools
Recommends:     iptables
Recommends:     socat

%{?systemd_requires}

%description
Kubernetes is a system for automating deployment, scaling, and management of
containerized applications. This package provides the core node, client, and
control-plane binaries used by kubeadm and manually managed clusters.

%prep
%autosetup -n %{name}-%{version}

%build
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-mod=vendor -trimpath -modcacherw"
export GOTOOLCHAIN=local
export KUBE_GIT_VERSION=v%{version}
export KUBE_GIT_MAJOR=1
export KUBE_GIT_MINOR=35
export KUBE_GIT_COMMIT=%{git_commit}
export KUBE_GIT_TREE_STATE=clean
export KUBE_BUILD_PLATFORMS="linux/$(go env GOARCH)"

make all WHAT="cmd/kubeadm cmd/kubectl cmd/kubelet cmd/kube-proxy cmd/kube-apiserver cmd/kube-controller-manager cmd/kube-scheduler"

%install
arch="$(go env GOARCH)"
bindirs="_output/bin _output/local/bin/linux/${arch} _output/local/go/bin"

for binary in kubeadm kubectl kubelet kube-proxy kube-apiserver kube-controller-manager kube-scheduler; do
    found=
    for bindir in ${bindirs}; do
        if [ -f "${bindir}/${binary}" ]; then
            found="${bindir}/${binary}"
            break
        fi
    done
    if [ -z "${found}" ]; then
        find _output -type f -name "${binary}" -print
        exit 1
    fi
    install -Dpm0755 "${found}" "%{buildroot}%{_bindir}/${binary}"
done

install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/kubelet.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_unitdir}/kubelet.service.d/10-kubeadm.conf
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/kubelet
install -dpm0755 %{buildroot}%{_localstatedir}/lib/kubelet

%check
%{buildroot}%{_bindir}/kubeadm version -o short
%{buildroot}%{_bindir}/kubectl version --client=true
%{buildroot}%{_bindir}/kubelet --version
%{buildroot}%{_bindir}/kube-proxy --version
%{buildroot}%{_bindir}/kube-apiserver --version
%{buildroot}%{_bindir}/kube-controller-manager --version
%{buildroot}%{_bindir}/kube-scheduler --version

%post
%systemd_post kubelet.service

%preun
%systemd_preun kubelet.service

%postun
%systemd_postun_with_restart kubelet.service

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_bindir}/kubeadm
%{_bindir}/kubectl
%{_bindir}/kubelet
%{_bindir}/kube-proxy
%{_bindir}/kube-apiserver
%{_bindir}/kube-controller-manager
%{_bindir}/kube-scheduler
%{_unitdir}/kubelet.service
%{_unitdir}/kubelet.service.d/10-kubeadm.conf
%config(noreplace) %{_sysconfdir}/sysconfig/kubelet
%dir %{_localstatedir}/lib/kubelet

%changelog
%autochangelog
