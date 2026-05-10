# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cifs-utils
Version:        7.5
Release:        %autorelease
Summary:        Utilities for mounting and managing CIFS mounts
License:        GPL-3.0-only
URL:            http://linux-cifs.samba.org/cifs-utils/
VCS:            git:git://git.samba.org/cifs-utils.git
#!RemoteAsset:  sha256:7face85e3d2d5eb5e7adbd181adee6759097f135b10d6fb30be8e070af7e7054
Source:         https://download.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --prefix=%{_prefix}
BuildOption(conf):  ROOTSBINDIR=%{_sbindir}
BuildOption(install):  DESTDIR=%{buildroot}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libkeyutils)
# for now,samba has not been packaged.
# BuildRequires:  libwbclient-devel
BuildRequires:  pkgconfig(pam)
BuildRequires:  make

Recommends:     %{name}-info

Requires:       keyutils
Requires(post): alternatives
Requires(preun):  alternatives

%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol.

%package        devel
Summary:        Files needed for building plugins for %{name}

%description    devel
This package contains the header file necessary for building ID mapping plugins
for cifs-utils.

%package     -n pam_cifscreds
Summary:        PAM module to manage NTLM credentials in kernel keyring

%description -n pam_cifscreds
The pam_cifscreds PAM module is a tool for automatically adding
credentials for multiuser mounts.

%package        info
Summary:        Additional tools for querying information about CIFS mounts
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    info
This subpackage includes additional tools for querying information
about CIFS mounts.

%conf -p
autoreconf -i

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.idmap.conf %{buildroot}%{_sysconfdir}/request-key.d
install -m 644 contrib/request-key.d/cifs.spnego.conf %{buildroot}%{_sysconfdir}/request-key.d

%post
alternatives --install /etc/cifs-utils/idmap-plugin cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so 10

%preun
if [ $1 = 0 ]; then
	alternatives --remove cifs-idmap-plugin %{_libdir}/%{name}/idmapwb.so
fi

%files
%license COPYING
%{_bindir}/cifscreds
%{_sbindir}/cifs.upcall
%{_sbindir}/mount.cifs
%{_sbindir}/mount.smb3
%dir %{_sysconfdir}/cifs-utils
%ghost %{_sysconfdir}/cifs-utils/idmap-plugin
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.idmap.conf
%config(noreplace) %{_sysconfdir}/request-key.d/cifs.spnego.conf

%files devel
%{_includedir}/cifsidmap.h

%files -n pam_cifscreds
%{_libdir}/security/pam_cifscreds.so

%files info
%{_bindir}/smb2-quota
%{_bindir}/smbinfo

%changelog
%autochangelog
