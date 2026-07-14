# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           msmtp
Version:        1.8.32
Release:        %autorelease
Summary:        msmtp is an SMTP client
License:        GPL-3.0-or-later
URL:            https://marlam.de/msmtp/
VCS:            git:https://git.marlam.de/gitweb/?p=msmtp.git
#!RemoteAsset:  sha256:20cd58b58dd007acf7b937fa1a1e21f3afb3e9ef5bbcfb8b4f5650deadc64db4
Source0:        https://marlam.de/msmtp/releases/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --with-libsecret

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libidn2)

Requires(post):  %{_sbindir}/alternatives
Requires(postun):  %{_sbindir}/alternatives

Provides:       %{_sbindir}/sendmail

%description
msmtp is an SMTP client. In the default mode, it transmits
a mail to an SMTP server which takes care of further delivery.

%conf -p
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages
# Remove the system-wide Info directory index, which must not be owned by an individual package.
rm -f %{buildroot}%{_infodir}/dir
# Remove the Sendmail compatibility links installed by upstream.
# These shared MTA entry points are managed through alternatives instead.
rm -f %{buildroot}%{_prefix}/lib/sendmail
rm -f %{buildroot}%{_sbindir}/sendmail
# Remove the newaliases compatibility command because msmtp does not
# maintain a local aliases database.
rm -f %{buildroot}%{_bindir}/newaliases
# Remove conflicting compatibility manual pages. The Sendmail manual-page
# entry is provided through alternatives together with the command.
rm -f %{buildroot}%{_mandir}/man1/sendmail.1*
rm -f %{buildroot}%{_mandir}/man1/newaliases.1*

%post
%{_sbindir}/alternatives --install %{_sbindir}/sendmail mta %{_bindir}/msmtp 40 \
  --slave %{_prefix}/lib/sendmail mta-sendmail %{_bindir}/msmtp \
  --slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man1/msmtp.1.gz

%postun
if [ "$1" -eq 0 ] ; then
    %{_sbindir}/alternatives --remove mta %{_bindir}/msmtp
fi

%files -f %{name}.lang
%doc AUTHORS NEWS README THANKS
%doc doc/msmtprc-system.example doc/msmtprc-user.example
%license COPYING
%{_bindir}/msmtp*
%{_infodir}/msmtp.info*
%{_mandir}/man1/msmtp*.1*
%ghost %{_sbindir}/sendmail
%ghost %{_prefix}/lib/sendmail
%ghost %{_mandir}/man8/sendmail.8.gz

%changelog
%autochangelog
