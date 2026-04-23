# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cloud-init
Version:        25.3
Release:        %autorelease
Summary:        Cloud instance init scripts
License:        Apache-2.0 OR GPL-3.0-only
URL:            https://github.com/canonical/cloud-init
#!RemoteAsset:  sha256:a6c0a28a4055d5cde35ac9249ad0596ee6aa10f0a29bd88a6e197d29adee0a3c
Source0:        https://github.com/canonical/cloud-init/archive/refs/tags/%{version}.tar.gz
Source1:        cloud-init.tmpfiles
BuildSystem:    meson

# skip some tests not support in build environment
Patch0:         0001-skip-crate-user-tests.patch

BuildOption(conf):  -Dinit_system=systemd
BuildOption(conf):  -Ddisable_sshd_keygen=true

BuildRequires:  meson
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  systemd-rpm-macros
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
# for tests
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(configobj)
BuildRequires:  python3dist(responses)
BuildRequires:  python3dist(jsonpatch)
BuildRequires:  python3dist(pyserial)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(packaging)

Requires:       python3
Requires:       python3dist(jinja2)
Requires:       python3dist(pyyaml)
Requires:       python3dist(requests)
Requires:       python3dist(selinux)
Requires:       python-policycoreutils
Requires:       dhcpcd
Requires:       iproute2
Requires:       hostname
Requires:       e2fsprogs
Requires:       shadow
Requires:       util-linux
Requires:       xfsprogs
Requires:       openssl
Requires:       python3dist(configobj)
Requires:       python3dist(jsonpatch)
Requires:       python3dist(jsonschema)
Requires:       python3dist(oauthlib)
Requires:       python3dist(pyserial)
%{?systemd_requires}

%description
Cloud-init is a set of init scripts for cloud instances. Cloud instances
need special scripts to run during initialization to retrieve and install
ssh keys and to let the user run various scripts.

%install -a
%py3_shebang_fix %{buildroot}%{_bindir}/

# /run/cloud-init needs a tmpfiles.d entry
mkdir -p %{buildroot}/var/lib/cloud
mkdir -p %{buildroot}/run/cloud-init

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -D -p -m 644 tools/21-cloudinit.conf %{buildroot}%{_sysconfdir}/rsyslog.d/21-cloudinit.conf

%pre
%tmpfiles_create_package %{name} %{SOURCE1}

%post
%systemd_post cloud-config.service cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service

%preun
%systemd_preun cloud-config.service cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service

%postun
%systemd_postun cloud-config.service cloud-final.service cloud-init-main.service cloud-init.target cloud-init-local.service cloud-init-network.service

%files
%license LICENSE LICENSE-Apache2.0 LICENSE-GPLv3
%doc ChangeLog doc/*
%{_bindir}/cloud-init*
%{_bindir}/cloud-id
%{_libexecdir}/cloud-init/
%{python3_sitelib}/cloudinit/
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg
%dir %{_sysconfdir}/cloud/cloud.cfg.d
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg.d/*.cfg
%doc %{_sysconfdir}/cloud/cloud.cfg.d/README
%dir %{_sysconfdir}/cloud/templates
%config(noreplace) %{_sysconfdir}/cloud/templates/*
%dir %{_sysconfdir}/rsyslog.d
%config(noreplace) %{_sysconfdir}/rsyslog.d/21-cloudinit.conf
%{_udevrulesdir}/*.rules
%{_unitdir}/*.service
%{_unitdir}/*.target
%{_unitdir}/*.socket
%{_unitdir}/sshd-keygen@.service.d/
%{_systemdgeneratordir}/cloud-init-generator
%{_tmpfilesdir}/cloud-init.conf
%{_datadir}/bash-completion/completions/cloud-init
%dir /run/cloud-init
%dir /var/lib/cloud

%changelog
%autochangelog
