# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond gnutls 1

Name:           swtpm
Version:        0.10.1
Release:        %autorelease
Summary:        TPM Emulator
License:        BSD-3-Clause
URL:            https://github.com/stefanberger/swtpm
#!RemoteAsset
Source:         https://github.com/stefanberger/swtpm/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --without-cuse
BuildOption(conf):  --disable-tests
BuildOption(conf):  --disable-static
%if %{with gnutls}
BuildOption(conf):  --with-gnutls
%endif

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(libtpms)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  glib-devel
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  socat
BuildRequires:  expect
BuildRequires:  pkgconfig(gmp)
%if %{with gnutls}
BuildRequires:  pkgconfig(gnutls)
%endif

Requires:       libtpms >= 0.10.0

%description
TPM emulator built on libtpms providing TPM functionality for QEMU VMs.

%package        devel
Summary:        Include files for the TPM emulator
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Include files for the TPM emulator.

%package        tests
Summary:        Installed swtpm tests
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tests
Installed swtpm tests.

%conf -p
NOCONFIGURE=1 ./autogen.sh

%files
%license LICENSE
%doc README
%{_bindir}/swtpm
%{_mandir}/man8/swtpm.8*
%dir %{_libdir}/swtpm
%{_libdir}/swtpm/libswtpm_libtpms.so.0*
%{_bindir}/swtpm_bios
%if %{with gnutls}
%{_bindir}/swtpm_cert
%endif
%{_bindir}/swtpm_setup
%{_bindir}/swtpm_ioctl
%{_bindir}/swtpm_localca
%{_mandir}/man5/swtpm*.5*
%{_mandir}/man8/swtpm_bios.8*
%{_mandir}/man8/swtpm_cert.8*
%{_mandir}/man8/swtpm_ioctl.8*
%{_mandir}/man8/swtpm-localca.8*
%{_mandir}/man8/swtpm_localca.8*
%{_mandir}/man8/swtpm_setup.8*
%config(noreplace) %{_sysconfdir}/swtpm_setup.conf
%config(noreplace) %{_sysconfdir}/swtpm-localca.options
%config(noreplace) %{_sysconfdir}/swtpm-localca.conf
%dir %{_datadir}/swtpm
%{_datadir}/swtpm/swtpm-localca
%{_datadir}/swtpm/swtpm-create-user-config-files
%attr(750, tss, root) %{_localstatedir}/lib/swtpm-localca
%{_mandir}/man8/swtpm-create-tpmca.8*
%{_datadir}/swtpm/swtpm-create-tpmca

%files devel
%dir %{_includedir}/swtpm
%{_includedir}/swtpm/*.h
%{_mandir}/man3/swtpm_ioctls.3*
%{_libdir}/swtpm/libswtpm_libtpms.so

%files tests
%{_libexecdir}/installed-tests/swtpm/

%changelog
%autochangelog
