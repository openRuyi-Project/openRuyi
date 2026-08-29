# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nano
Version:        9.0
Release:        %autorelease
Summary:        Text editor
License:        GPL-3.0-or-later
URL:            https://www.nano-editor.org
VCS:            git:https://https.git.savannah.gnu.org/git/nano.git
#!RemoteAsset:  sha256:9f384374b496110a25b73ad5a5febb384783c6e3188b37063f677ac908013fde
Source0:        https://www.nano-editor.org/dist/latest/%{name}-%{version}.tar.xz
Source2:        nanorc
BuildSystem:    autotools

BuildOption(conf):  --enable-color
BuildOption(conf):  --enable-nanorc
BuildOption(conf):  --enable-multibuffer
BuildOption(conf):  --enable-utf8

BuildRequires:  pkgconfig(libmagic)
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  texinfo

%description
GNU nano is a small and friendly text editor.

%build -a
# Enable syntax highlighting by default - 251
sed -E -e 's|^# (include "?/usr/share/nano/\*.nanorc"?)|\1|' \
    %{SOURCE2} doc/sample.nanorc > ./nanorc

%install -a
# Install our /etc/nanorc - 251
mkdir -p %{buildroot}%{_sysconfdir}
install -m 0644 ./nanorc %{buildroot}%{_sysconfdir}/nanorc
%find_lang %{name} --generate-subpackages

%files
%license COPYING COPYING.DOC
%doc AUTHORS ChangeLog* IMPROVEMENTS NEWS README THANKS TODO
%doc doc/{faq,nano}.html
%{_bindir}/{,r}nano
%config(noreplace) %{_sysconfdir}/nanorc
%{_mandir}/man1/{,r}nano.1*
%{_mandir}/man5/nanorc.5*
%{_infodir}/nano.info*
%{_datadir}/nano

%changelog
%autochangelog
