# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Summary:        Dynamic Kernel Module Support Framework
Name:           dkms
Version:        3.2.2
Release:        %autorelease
License:        GPL-2.0-or-later
URL:            http://linux.dell.com/dkms
VCS:            git:https://github.com/dkms-project/dkms
#!RemoteAsset
Source0:        https://github.com/dkms-project/dkms/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       coreutils
Requires:       cpio
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       grep
Requires:       gzip
Requires:       kmod
Requires:       make
Requires:       patch
Requires:       sed
Requires:       tar
Requires:       which

%{?systemd_requires}

Recommends:     openssl

%description
This package contains the framework for the Dynamic Kernel Module Support (DKMS)
method for installing module RPMS as originally developed by Dell.

%prep
%autosetup -p1

%install
make install-redhat \
    SBIN=%{_sbindir} \
    DESTDIR=%{buildroot}

sed -i \
    -e 's/# modprobe_on_install.*/modprobe_on_install="true"/g' \
    -e 's/# post_transaction.*/post_transaction="dracut --regenerate-all --force"/g' \
    %{buildroot}%{_sysconfdir}/dkms/framework.conf

%post
%systemd_post dkms.service

%preun
%systemd_preun dkms.service

%postun
%systemd_postun dkms.service

%files
%license COPYING
%doc README.md images
%{_prefix}/lib/dkms
%{_prefix}/lib/kernel/install.d/40-dkms.install
%{_mandir}/man8/dkms.8*
%{_sbindir}/dkms
%{_sharedstatedir}/dkms
%dir %{_sysconfdir}/dkms
%config(noreplace) %{_sysconfdir}/dkms/framework.conf
%dir %{_sysconfdir}/dkms/framework.conf.d
%{_datadir}/bash-completion/completions/dkms
%{_datadir}/zsh/site-functions/_dkms
%{_unitdir}/dkms.service

%changelog
%autochangelog
