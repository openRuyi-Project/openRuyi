# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           fonts-codenewroman-nerd
Version:        3.4.0
Release:        %autorelease
Summary:        Code New Roman Nerd Font
License:        OFL-1.1
URL:            https://www.nerdfonts.com/
VCS:            git:https://github.com/ryanoasis/nerd-fonts.git
#!RemoteAsset:  sha256:2db8def7863ea49b6ef69f353988d7e0f73a8646722e5946932740d76eb46b25
Source0:        https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/CodeNewRoman.tar.xz
BuildArch:      noarch

%description
Code New Roman Nerd Font is a patched version of Code New Roman with icons
from Nerd Fonts.

%prep
%autosetup -c

%build
# No build required

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/opentype/codenewroman-nerd
install -m 0644 -p *.otf %{buildroot}%{_datadir}/fonts/opentype/codenewroman-nerd/

%files
%doc README.md
%license license.txt
%dir %{_datadir}/fonts/opentype/codenewroman-nerd/
%{_datadir}/fonts/opentype/codenewroman-nerd/*.otf

%changelog
%autochangelog
