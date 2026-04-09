# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mailcap
Version:        2.1.54
Release:        %autorelease
Summary:        Helper application and MIME type associations for file types
License:        LicenseRef-openRuyi-Public-Domain AND MIT AND metamail
URL:            https://pagure.io/mailcap
#!RemoteAsset
Source0:        https://pagure.io/releases/mailcap/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  python3

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.  Mailcap should be installed to allow
certain programs to be able to handle non-text files.

Also included in this package is the mime.types file which contains a
list of MIME types and their filename "extension" associations, used
by several applications e.g. to determine MIME types for filenames.

%package     -n nginx-mimetypes
Summary:        MIME type mappings for nginx
License:        LicenseRef-openRuyi-Public-Domain


%description -n nginx-mimetypes
MIME type mappings for nginx.

%conf
# No configuration needed

%files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man5/mailcap.*

%files -n nginx-mimetypes
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/nginx/mime.types

%changelog
%autochangelog
