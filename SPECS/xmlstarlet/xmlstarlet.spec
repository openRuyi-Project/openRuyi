# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           xmlstarlet
Version:        1.6.1
Release:        %autorelease
Summary:        Command line XML toolkit
License:        MIT
URL:            https://xmlstar.sourceforge.net/
VCS:            git:https://git.code.sf.net/p/xmlstar/code
#!RemoteAsset:  sha256:15d838c4f3375332fd95554619179b69e4ec91418a3a5296e7c631b7ed19e7ca
Source0:        https://downloads.sourceforge.net/xmlstar/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)

%patchlist
# disable entity expansion to prevent XXE attacks, and mark tests broken
# by newer libxml2 as expected failures
# https://src.fedoraproject.org/rpms/xmlstarlet/blob/rawhide/f/xmlstarlet-1.6.1-fix-xxe.patch
1000-fix-xxe.patch
# libxml2 2.13 removed ATTRIBUTE_UNUSED from its public headers
2000-Define-ATTRIBUTE_UNUSED-fallback-for-libxml2-2.13.patch

%description
XMLStarlet is a set of command line utilities (tools) which can be used
to transform, query, validate, and edit XML documents and files using a
simple set of shell commands in a way similar to how it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc.

%conf -p
autoreconf -fiv

%install -a
# upstream installs the binary under the generic name xml
mv %{buildroot}%{_bindir}/xml %{buildroot}%{_bindir}/xmlstarlet

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_pkgdocdir}/html.css
%doc %{_pkgdocdir}/xmlstarlet-ug.html
%doc %{_pkgdocdir}/xmlstarlet.txt
%license COPYING
%{_bindir}/xmlstarlet
%{_mandir}/man1/xmlstarlet.1*

%changelog
%autochangelog
