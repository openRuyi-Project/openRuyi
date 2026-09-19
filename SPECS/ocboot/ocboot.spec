# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# UTC timestamp of the commit referenced by the upstream v4.0.3 tag.
%global source_date_epoch  1779875922

Name:           ocboot
Version:        4.0.3
Release:        %autorelease
Summary:        Cloudpods deployment and lifecycle management tool
License:        Apache-2.0 AND MulanPSL-2.0
URL:            https://github.com/yunionio/ocboot
VCS:            git:https://github.com/yunionio/ocboot.git
#!RemoteAsset:  sha256:6f64664f7cb49375be73fb12633f7d850b6468ffe67b5d801d802cb58bd081d0
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        ocboot
# Add openEuler riscv64 and explicit external artifact support. Drop after
# upstream PR #1707 is merged and released.
Patch2000:      2000-feat-support-openEuler-riscv64-deployments.patch
# Resolve resources relative to the installed source tree while preserving the
# caller's working directory for configuration inputs.
Patch2001:      2001-fix-support-installed-ocboot-source-layouts.patch
BuildArch:      noarch

BuildRequires:  bash
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pyyaml)
Requires:       bash
Requires:       buildah
Requires:       sudo
Recommends:     openssh-clients

Provides:       onecloud-ocboot = %{version}-%{release}

%description
ocboot deploys and manages Cloudpods clusters through a Buildah-hosted
Ansible environment. This package includes the deployment playbooks, helper
scripts, and explicit openEuler RISC-V artifact configuration support.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export SOURCE_DATE_EPOCH=%{source_date_epoch}

%install
install -dm0755 %{buildroot}%{_libexecdir}/%{name}
cp -a . %{buildroot}%{_libexecdir}/%{name}/
find %{buildroot}%{_libexecdir}/%{name} -type d -name __pycache__ -prune -exec rm -rf {} +
find %{buildroot}%{_libexecdir}/%{name} -type f -name '*.py[co]' -delete
rm -rf %{buildroot}%{_libexecdir}/%{name}/{.github,tests}
rm -f %{buildroot}%{_libexecdir}/%{name}/{Dockerfile,LICENSE,Makefile,README.md,TODO.md}

install -Dm0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%check
export USER=root
export LOGNAME=root
# Run the upstream suite together with the RISC-V configuration and artifact
# validation tests carried by Patch2000.
python3 -m unittest discover -s tests -v
# Parse every shipped shell entry point and verify the installed layout keeps
# both the launcher and required RISC-V deployment resources.
find . -type f -name '*.sh' -print0 | xargs -0 -n1 bash -n
test -x %{buildroot}%{_bindir}/%{name}
test -x %{buildroot}%{_libexecdir}/%{name}/ocboot.sh
grep -q 'riscv64)' %{buildroot}%{_libexecdir}/%{name}/airgap_assets/k3s-install.sh
grep -q 'is_openeuler_riscv64: true' %{buildroot}%{_libexecdir}/%{name}/onecloud/roles/utils/detect-os/vars/openeuler-riscv64.yml

%files
%doc README.md docs/riscv64.md
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
%autochangelog
