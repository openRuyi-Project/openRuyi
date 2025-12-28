# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libiscsi
Summary:        iSCSI client library
Version:        1.20.3
Release:        %autorelease
License:        LGPL-2.1-or-later
URL:            https://github.com/sahlberg/libiscsi
#!RemoteAsset
Source:         https://github.com/sahlberg/libiscsi/archive/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-werror
BuildOption(conf):  --with-gnutls

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  rdma-core-devel

%description
libiscsi is a library for attaching to iSCSI resources across
a network.

%conf -p
./autogen.sh

%install -a
rm $RPM_BUILD_ROOT/%{_libdir}/libiscsi.a

%package        devel
Summary:        iSCSI client development libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libiscsi-devel package includes the header files for libiscsi.

%package        utils
Summary:        iSCSI Client Utilities
License:        GPL-2.0-or-later

%description    utils
The libiscsi-utils package provides a set of assorted utilities to connect
to iSCSI servers without having to set up the Linux iSCSI initiator.

%files
%license COPYING LICENCE-LGPL-2.1.txt
%doc README.md TODO
%{_libdir}/libiscsi.so.11*

%files devel
%dir %{_includedir}/iscsi
%{_includedir}/iscsi/iscsi.h
%{_includedir}/iscsi/scsi-lowlevel.h
%{_libdir}/libiscsi.so
%{_libdir}/pkgconfig/libiscsi.pc

%files utils
%license LICENCE-GPL-2.txt
%{_bindir}/iscsi-ls
%{_bindir}/iscsi-inq
%{_bindir}/iscsi-readcapacity16
%{_bindir}/iscsi-swp
%{_bindir}/iscsi-perf
%{_bindir}/iscsi-test-cu
%{_bindir}/iscsi-pr
%{_bindir}/iscsi-discard
%{_bindir}/iscsi-md5sum
%{_bindir}/iscsi-rtpg
%{_mandir}/man1/iscsi-ls.1.gz
%{_mandir}/man1/iscsi-inq.1.gz
%{_mandir}/man1/iscsi-swp.1.gz
%{_mandir}/man1/iscsi-test-cu.1.gz
%{_mandir}/man1/iscsi-md5sum.1.gz

%changelog
%{?autochangelog}
