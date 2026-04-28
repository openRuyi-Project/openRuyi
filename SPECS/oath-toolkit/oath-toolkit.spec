# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           oath-toolkit
Version:        2.6.14
Release:        %autorelease
Summary:        One-time password components
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
URL:            https://www.nongnu.org/oath-toolkit/
VCS:            git:https://git.savannah.nongnu.org/git/oath-toolkit.git
#!RemoteAsset:  sha256:8b1da365759f1249be57a82aec6e107f7b57dc77d813f96dc0aaf81624f28971
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --with-pam-dir=%{_libdir}/security
BuildOption(conf):  --disable-gtk-doc
BuildOption(conf):  --disable-gtk-doc-html
BuildOption(conf):  --disable-gtk-doc-pdf
BuildOption(conf):  --without-xmlsec

BuildRequires:  make
BuildRequires:  pkgconfig(pam)
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake

Provides:       liboath = %{version}-%{release}
Provides:       liboath%{?_isa} = %{version}-%{release}

%description
The OATH Toolkit provide components for building one-time password
authentication systems. It contains shared libraries, command line tools and a
PAM module. Supported technologies include the event-based HOTP algorithm
(RFC4226) and the time-based TOTP algorithm (RFC6238). OATH stands for Open
AuTHentication, which is the organization that specify the algorithms. For
managing secret key files, the Portable Symmetric Key Container (PSKC) format
described in RFC6030 is supported.

%package     -n pam_oath
Summary:        A PAM module for pluggable login authentication for OATH
Requires:       pam

%description -n pam_oath
A PAM module for pluggable login authentication for OATH.

%build -p

# Kill rpaths and link with --as-needed
# Only process directories that actually exist
for d in liboath pam_oath
do
  if [ -f $d/libtool ]; then
    sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $d/libtool
    sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $d/libtool
    sed -i 's| -shared | -Wl,--as-needed\0|g' $d/libtool
  fi
done

%install -a

# no test
%check

# Remove static objects
rm -f %{buildroot}%{_libdir}/*.a

# Make /etc/liboath directory
mkdir -p -m 0600 %{buildroot}%{_sysconfdir}/liboath

%files
%doc COPYING
%{_bindir}/oathtool
%{_mandir}/man1/oathtool.*
# liboath runtime libs
%attr(0600, root, root) %dir %{_sysconfdir}/liboath
%{_libdir}/liboath.so.*
# liboath devel files
%{_includedir}/liboath
%{_libdir}/liboath.so
%{_libdir}/pkgconfig/liboath.pc
%{_mandir}/man3/oath*
%{_datadir}/gtk-doc/html/liboath/*

%files -n pam_oath
%doc pam_oath/README COPYING
%{_libdir}/security/pam_oath.so

%changelog
%autochangelog
