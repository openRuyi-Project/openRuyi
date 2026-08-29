# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yihong <yihong.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gophercloud
%define go_import_path  github.com/gophercloud/gophercloud/v2

Name:           go-github-gophercloud-gophercloud-v2
Version:        2.12.0
Release:        %autorelease
Summary:        OpenStack SDK for Go
License:        Apache-2.0
URL:            https://github.com/gophercloud/gophercloud
#!RemoteAsset:  sha256:cb9b18d8d1efb4be3955d0706db97369c94e30fa05b13669c9f0feb1d40f75c3
Source0:        https://github.com/gophercloud/gophercloud/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(gopkg.in/yaml.v2)

# gophercloud ships 474 importable packages. Per the openRuyi
# prometheus-go-tail-deps effort this package only needs to satisfy the
# import paths actually pulled in by Prometheus' OpenStack service
# discovery; those are enumerated below. The full source tree is still
# installed under %{go_sys_gopath}, so additional paths resolve from the
# on-disk sources even when not listed as virtual Provides.
Provides:       go(github.com/gophercloud/gophercloud/v2) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/compute/v2/hypervisors) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/compute/v2/servers) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/identity/v2/tenants) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/identity/v2/tokens) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/identity/v3/ec2tokens) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/identity/v3/oauth1) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/identity/v3/tokens) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/loadbalancer/v2/l7policies) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/loadbalancer/v2/listeners) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/loadbalancer/v2/loadbalancers) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/loadbalancer/v2/monitors) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/loadbalancer/v2/pools) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/networking/v2/extensions/layer3/floatingips) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/networking/v2/ports) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/openstack/utils) = %{version}
Provides:       go(github.com/gophercloud/gophercloud/v2/pagination) = %{version}

Requires:       go(golang.org/x/crypto)
Requires:       go(gopkg.in/yaml.v2)

%description
Gophercloud is an OpenStack Go SDK. It provides typed clients for the
OpenStack Identity, Compute, Networking and Load Balancer APIs and is
used by Prometheus' OpenStack service discovery.

%files
%doc README*
%license LICENSE*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
