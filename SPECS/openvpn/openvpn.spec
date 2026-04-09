# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond dco 0
%bcond pkcs11 0

Name:           openvpn
Version:        2.6.16
Release:        %autorelease
Summary:        A full-featured TLS VPN solution
License:        GPL-2.0-only
URL:            https://community.openvpn.net/
VCS:            git:https://github.com/OpenVPN/openvpn
#!RemoteAsset
Source0:        https://github.com/OpenVPN/openvpn/archive/refs/tags/v%{version}.tar.gz
Source1:        roadwarrior-server.conf
Source2:        roadwarrior-client.conf
Source3:        openvpn.sysusers
BuildSystem:    autotools

BuildOption(conf):  --enable-silent-rules
BuildOption(conf):  --with-crypto-library=openssl
BuildOption(conf):  --enable-selinux
BuildOption(conf):  --enable-systemd
BuildOption(conf):  --enable-x509-alt-username
BuildOption(conf):  --enable-async-push
BuildOption(conf):  --docdir=%{_pkgdocdir}
BuildOption(conf):  SYSTEMD_UNIT_DIR=%{_unitdir}
BuildOption(conf):  TMPFILES_DIR=%{_tmpfilesdir}
%if %{with pkcs11}
BuildOption(conf):  --enable-pkcs11
%endif
%if %{without dco}
BuildOption(conf):  --disable-dco
%endif

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  python3-docutils
BuildRequires:  pkgconfig(python3)
%if %{with dco}
BuildRequires:  pkgconfig(libnl-3.0)
%endif
%if %{with pkcs11}
BuildRequires:  pkcs11-helper-devel >= 1.11
%endif

%{?systemd_requires}
Requires(post): /usr/bin/awk

%description
OpenVPN is a robust and highly flexible tunneling application that uses all
of the encryption, authentication, and certification features of the
OpenSSL library to securely tunnel IP networks over a single UDP or TCP
port.

%package        devel
Summary:        Development headers and examples for OpenVPN plug-ins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
OpenVPN can be extended through the --plugin option. This package contains
header files for developing such plugins.

%prep -a
# %%doc items shouldn't be executable.
find contrib sample -type f -perm /100 -exec chmod a-x {} \;

%conf -p
autoreconf -fiv

# Disable check.
%check

%install -a
mkdir -p -m 0750 %{buildroot}%{_sysconfdir}/%{name}/client %{buildroot}%{_sysconfdir}/%{name}/server
cp %{SOURCE1} %{SOURCE2} sample/sample-config-files/

# Create some directories the OpenVPN package should own
mkdir -m 0750 -p %{buildroot}%{_rundir}/%{name}-{client,server}
mkdir -m 0770 -p %{buildroot}%{_sharedstatedir}/%{name}

# Create a sysusers.d config file
install -m0644 -D %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

# Package installs into %%{_pkgdocdir} directly
# Add various additional files
cp -a AUTHORS ChangeLog contrib sample distro/systemd/README.systemd %{buildroot}%{_pkgdocdir}

%py3_shebang_fix %{buildroot}%{_pkgdocdir}

# Remove some files which does not really belong here
rm -f  %{buildroot}%{_pkgdocdir}/sample/Makefile{,.in,.am}
rm -f  %{buildroot}%{_pkgdocdir}/sample/sample-plugins/Makefile{,.in,.am}
rm -rf %{buildroot}%{_pkgdocdir}/sample/sample-keys
rm -f  %{buildroot}%{_pkgdocdir}/contrib/multilevel-init.patch
rm -rf %{buildroot}%{_pkgdocdir}/contrib/vcpkg-*
rm -rf %{buildroot}%{_pkgdocdir}/contrib/cmake*

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post openvpn-client@.service openvpn-server@.service

%preun
%systemd_preun openvpn-client@.service openvpn-server@.service

%postun
%systemd_postun_with_restart openvpn-client@.service openvpn-server@.service

%files
%license COPYING COPYRIGHT.GPL
%exclude %{_pkgdocdir}/COPYING
%exclude %{_pkgdocdir}/COPYRIGHT.GPL
%exclude %{_pkgdocdir}/README.mbedtls
%exclude %{_pkgdocdir}/sample/sample-plugins
%{_pkgdocdir}/
%{_mandir}/man8/openvpn.8*
%{_mandir}/man5/openvpn-*.5*
%{_sbindir}/openvpn
%{_libdir}/openvpn/
%{_unitdir}/openvpn-client@.service
%{_unitdir}/openvpn-server@.service
%{_tmpfilesdir}/openvpn.conf
%{_sysusersdir}/openvpn.conf
%config %dir %{_sysconfdir}/openvpn/
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/openvpn/client
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/openvpn/server
%attr(0770,openvpn,openvpn) %{_sharedstatedir}/openvpn
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-client
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-server

%files devel
%{_pkgdocdir}/sample/sample-plugins
%exclude %{_pkgdocdir}/sample/sample-{config-files,scripts,windows}
%{_includedir}/openvpn-plugin.h
%{_includedir}/openvpn-msg.h

%changelog
%autochangelog
