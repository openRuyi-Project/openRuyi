# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-ui-kit
%global full_version 0.3.2
%global pkgname objc2-ui-kit-0.3

Name:           rust-objc2-ui-kit-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-ui-kit"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:d87d638e33c06f577498cbcc50491496a3ed4246998a7fbba7ccb98b1e7eab22
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/documentmanager)
Provides:       crate(%{pkgname}/nsfileproviderextension)
Provides:       crate(%{pkgname}/nstext)
Provides:       crate(%{pkgname}/nstextviewportlayoutcontroller)
Provides:       crate(%{pkgname}/nstoolbar-uikitadditions)
Provides:       crate(%{pkgname}/nstouchbar-uikitadditions)
Provides:       crate(%{pkgname}/nsuseractivity-nsitemprovider)
Provides:       crate(%{pkgname}/printkitui)
Provides:       crate(%{pkgname}/sharesheet)
Provides:       crate(%{pkgname}/uiaccessibilitycontentsizecategoryimageadjusting)
Provides:       crate(%{pkgname}/uiaccessibilityzoom)
Provides:       crate(%{pkgname}/uialert)
Provides:       crate(%{pkgname}/uibandselectioninteraction)
Provides:       crate(%{pkgname}/uibarcommon)
Provides:       crate(%{pkgname}/uibehavioralstyle)
Provides:       crate(%{pkgname}/uicalendarselection)
Provides:       crate(%{pkgname}/uicalendarviewdecoration)
Provides:       crate(%{pkgname}/uicanvasfeedbackgenerator)
Provides:       crate(%{pkgname}/uiconfigurationcolortransformer)
Provides:       crate(%{pkgname}/uicontentsizecategoryadjusting)
Provides:       crate(%{pkgname}/uicontextmenusystem)
Provides:       crate(%{pkgname}/uifeedbackgenerator)
Provides:       crate(%{pkgname}/uifocusdebugger)
Provides:       crate(%{pkgname}/uifocusdefines)
Provides:       crate(%{pkgname}/uifocussystem)
Provides:       crate(%{pkgname}/uifocusupdatecontext-uikitadditions)
Provides:       crate(%{pkgname}/uifoundation)
Provides:       crate(%{pkgname}/uiguidedaccessrestrictions)
Provides:       crate(%{pkgname}/uiimpactfeedbackgenerator)
Provides:       crate(%{pkgname}/uiinputsuggestion)
Provides:       crate(%{pkgname}/uiinterface)
Provides:       crate(%{pkgname}/uikeyconstants)
Provides:       crate(%{pkgname}/uikitcore)
Provides:       crate(%{pkgname}/uikitdefines)
Provides:       crate(%{pkgname}/uiletterformawareadjusting)
Provides:       crate(%{pkgname}/uimenusystem)
Provides:       crate(%{pkgname}/uimessageconversationcontext)
Provides:       crate(%{pkgname}/uimessageconversationentry)
Provides:       crate(%{pkgname}/uinibdeclarations)
Provides:       crate(%{pkgname}/uinotificationfeedbackgenerator)
Provides:       crate(%{pkgname}/uipointerinteraction)
Provides:       crate(%{pkgname}/uipopoverpresentationcontrollersourceitem)
Provides:       crate(%{pkgname}/uipresentationcontroller)
Provides:       crate(%{pkgname}/uipreviewinteraction)
Provides:       crate(%{pkgname}/uiresponder-uiactivityitemsconfiguration)
Provides:       crate(%{pkgname}/uisceneenhancedstaterestoration)
Provides:       crate(%{pkgname}/uiscenesizerestrictions)
Provides:       crate(%{pkgname}/uiscenewindowingbehaviors)
Provides:       crate(%{pkgname}/uiscenewindowingcontrolstyle)
Provides:       crate(%{pkgname}/uiscene-avaudiosession)
Provides:       crate(%{pkgname}/uiscreenmode)
Provides:       crate(%{pkgname}/uiscribbleinteraction)
Provides:       crate(%{pkgname}/uiscrolledgeelementcontainerinteraction)
Provides:       crate(%{pkgname}/uiselectionfeedbackgenerator)
Provides:       crate(%{pkgname}/uisnapbehavior)
Provides:       crate(%{pkgname}/uisplitviewcontrollerlayoutenvironment)
Provides:       crate(%{pkgname}/uispringloadedinteraction)
Provides:       crate(%{pkgname}/uispringloadedinteractionsupporting)
Provides:       crate(%{pkgname}/uistatusbarmanager)
Provides:       crate(%{pkgname}/uisymboleffectcompletion)
Provides:       crate(%{pkgname}/uitabaccessory)
Provides:       crate(%{pkgname}/uitextcursordroppositionanimator)
Provides:       crate(%{pkgname}/uitextcursorview)
Provides:       crate(%{pkgname}/uitextinputcontext)
Provides:       crate(%{pkgname}/uitextiteminteraction)
Provides:       crate(%{pkgname}/uitextloupesession)
Provides:       crate(%{pkgname}/uitextpasteconfigurationsupporting)
Provides:       crate(%{pkgname}/uitextselectionhandleview)
Provides:       crate(%{pkgname}/uitraitlistenvironment)
Provides:       crate(%{pkgname}/uiupdateactionphase)
Provides:       crate(%{pkgname}/uiupdatelink)
Provides:       crate(%{pkgname}/uiviewcontrollertransition)
Provides:       crate(%{pkgname}/uiviewlayoutregion)
Provides:       crate(%{pkgname}/uiwindowsceneactivationrequestoptions)
Provides:       crate(%{pkgname}/uiwindowscenedraginteraction)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferences)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesios)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesmac)
Provides:       crate(%{pkgname}/uiwindowscenegeometrypreferencesvision)
Provides:       crate(%{pkgname}/uiwritingtoolscoordinatoranimationparameters)
Provides:       crate(%{pkgname}/unnotificationresponse-uikitadditions)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-ui-kit"

%package     -n %{name}+nsadaptiveimageglyph
Summary:        Bindings to the UIKit framework - feature "NSAdaptiveImageGlyph"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsadaptiveimageglyph)

%description -n %{name}+nsadaptiveimageglyph
This metapackage enables feature "NSAdaptiveImageGlyph" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsattributedstring
Summary:        Bindings to the UIKit framework - feature "NSAttributedString"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilewrapper) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsattributedstring)

%description -n %{name}+nsattributedstring
This metapackage enables feature "NSAttributedString" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdataasset
Summary:        Bindings to the UIKit framework - feature "NSDataAsset"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsdataasset)

%description -n %{name}+nsdataasset
This metapackage enables feature "NSDataAsset" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdiffabledatasourcesectionsnapshot
Summary:        Bindings to the UIKit framework - feature "NSDiffableDataSourceSectionSnapshot" and 5 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsdiffabledatasourcesectionsnapshot)
Provides:       crate(%{pkgname}/nslayoutanchor)
Provides:       crate(%{pkgname}/uifont)
Provides:       crate(%{pkgname}/uilexicon)
Provides:       crate(%{pkgname}/uislidertrackconfiguration)
Provides:       crate(%{pkgname}/uitextformattingviewcontrollercomponent)

%description -n %{name}+nsdiffabledatasourcesectionsnapshot
This metapackage enables feature "NSDiffableDataSourceSectionSnapshot" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSLayoutAnchor", "UIFont", "UILexicon", "UISliderTrackConfiguration", and "UITextFormattingViewControllerComponent" features.

%package     -n %{name}+nsindexpath-uikitadditions
Summary:        Bindings to the UIKit framework - feature "NSIndexPath_UIKitAdditions" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Provides:       crate(%{pkgname}/nsindexpath-uikitadditions)
Provides:       crate(%{pkgname}/uicollectionviewupdateitem)
Provides:       crate(%{pkgname}/uidatasourcetranslating)

%description -n %{name}+nsindexpath-uikitadditions
This metapackage enables feature "NSIndexPath_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICollectionViewUpdateItem", and "UIDataSourceTranslating" features.

%package     -n %{name}+nsitemprovider-uikitadditions
Summary:        Bindings to the UIKit framework - feature "NSItemProvider_UIKitAdditions"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsitemprovider-uikitadditions)

%description -n %{name}+nsitemprovider-uikitadditions
This metapackage enables feature "NSItemProvider_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nslayoutconstraint
Summary:        Bindings to the UIKit framework - feature "NSLayoutConstraint"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nslayoutconstraint)

%description -n %{name}+nslayoutconstraint
This metapackage enables feature "NSLayoutConstraint" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nslayoutmanager
Summary:        Bindings to the UIKit framework - feature "NSLayoutManager"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nslayoutmanager)

%description -n %{name}+nslayoutmanager
This metapackage enables feature "NSLayoutManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsparagraphstyle
Summary:        Bindings to the UIKit framework - feature "NSParagraphStyle"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscharacterset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsparagraphstyle)

%description -n %{name}+nsparagraphstyle
This metapackage enables feature "NSParagraphStyle" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsshadow
Summary:        Bindings to the UIKit framework - feature "NSShadow" and 18 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsshadow)
Provides:       crate(%{pkgname}/uiactivityindicatorview)
Provides:       crate(%{pkgname}/uibackgroundextensionview)
Provides:       crate(%{pkgname}/uibarappearance)
Provides:       crate(%{pkgname}/uibezierpath)
Provides:       crate(%{pkgname}/uicellconfigurationstate)
Provides:       crate(%{pkgname}/uicontentunavailableview)
Provides:       crate(%{pkgname}/uieventattributionview)
Provides:       crate(%{pkgname}/uiimageasset)
Provides:       crate(%{pkgname}/uiinputview)
Provides:       crate(%{pkgname}/uipagecontrol)
Provides:       crate(%{pkgname}/uipastecontrol)
Provides:       crate(%{pkgname}/uipopoverbackgroundview)
Provides:       crate(%{pkgname}/uislider)
Provides:       crate(%{pkgname}/uistandardtextcursorview)
Provides:       crate(%{pkgname}/uistepper)
Provides:       crate(%{pkgname}/uitoolbarappearance)
Provides:       crate(%{pkgname}/uiviewconfigurationstate)
Provides:       crate(%{pkgname}/uivisualeffectview)

%description -n %{name}+nsshadow
This metapackage enables feature "NSShadow" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActivityIndicatorView", "UIBackgroundExtensionView", "UIBarAppearance", "UIBezierPath", "UICellConfigurationState", "UIContentUnavailableView", "UIEventAttributionView", "UIImageAsset", "UIInputView", "UIPageControl", "UIPasteControl", "UIPopoverBackgroundView", "UISlider", "UIStandardTextCursorView", "UIStepper", "UIToolbarAppearance", "UIViewConfigurationState", and "UIVisualEffectView" features.

%package     -n %{name}+nsstringdrawing
Summary:        Bindings to the UIKit framework - feature "NSStringDrawing"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsstringdrawing)

%description -n %{name}+nsstringdrawing
This metapackage enables feature "NSStringDrawing" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextattachment
Summary:        Bindings to the UIKit framework - feature "NSTextAttachment"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilewrapper) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextattachment)

%description -n %{name}+nstextattachment
This metapackage enables feature "NSTextAttachment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextcontainer
Summary:        Bindings to the UIKit framework - feature "NSTextContainer" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nstextcontainer)
Provides:       crate(%{pkgname}/uicollectionviewlistcell)
Provides:       crate(%{pkgname}/uistackview)
Provides:       crate(%{pkgname}/uitabbar)
Provides:       crate(%{pkgname}/uitoolbar)

%description -n %{name}+nstextcontainer
This metapackage enables feature "NSTextContainer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICollectionViewListCell", "UIStackView", "UITabBar", and "UIToolbar" features.

%package     -n %{name}+nstextcontentmanager
Summary:        Bindings to the UIKit framework - feature "NSTextContentManager"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextcontentmanager)

%description -n %{name}+nstextcontentmanager
This metapackage enables feature "NSTextContentManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextelement
Summary:        Bindings to the UIKit framework - feature "NSTextElement"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextelement)

%description -n %{name}+nstextelement
This metapackage enables feature "NSTextElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutfragment
Summary:        Bindings to the UIKit framework - feature "NSTextLayoutFragment"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlayoutfragment)

%description -n %{name}+nstextlayoutfragment
This metapackage enables feature "NSTextLayoutFragment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutmanager
Summary:        Bindings to the UIKit framework - feature "NSTextLayoutManager"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlayoutmanager)

%description -n %{name}+nstextlayoutmanager
This metapackage enables feature "NSTextLayoutManager" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlinefragment
Summary:        Bindings to the UIKit framework - feature "NSTextLineFragment"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlinefragment)

%description -n %{name}+nstextlinefragment
This metapackage enables feature "NSTextLineFragment" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlist
Summary:        Bindings to the UIKit framework - feature "NSTextList" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlist)
Provides:       crate(%{pkgname}/uimenuelement)
Provides:       crate(%{pkgname}/uitableviewcell)

%description -n %{name}+nstextlist
This metapackage enables feature "NSTextList" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMenuElement", and "UITableViewCell" features.

%package     -n %{name}+nstextlistelement
Summary:        Bindings to the UIKit framework - feature "NSTextListElement"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextlistelement)

%description -n %{name}+nstextlistelement
This metapackage enables feature "NSTextListElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextrange
Summary:        Bindings to the UIKit framework - feature "NSTextRange"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Provides:       crate(%{pkgname}/nstextrange)

%description -n %{name}+nstextrange
This metapackage enables feature "NSTextRange" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextselection
Summary:        Bindings to the UIKit framework - feature "NSTextSelection" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextselection)
Provides:       crate(%{pkgname}/uinavigationbar)
Provides:       crate(%{pkgname}/uisegmentedcontrol)

%description -n %{name}+nstextselection
This metapackage enables feature "NSTextSelection" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UINavigationBar", and "UISegmentedControl" features.

%package     -n %{name}+nstextselectionnavigation
Summary:        Bindings to the UIKit framework - feature "NSTextSelectionNavigation"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextselectionnavigation)

%description -n %{name}+nstextselectionnavigation
This metapackage enables feature "NSTextSelectionNavigation" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextstorage
Summary:        Bindings to the UIKit framework - feature "NSTextStorage"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nstextstorage)

%description -n %{name}+nstextstorage
This metapackage enables feature "NSTextStorage" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccelerometer
Summary:        Bindings to the UIKit framework - feature "UIAccelerometer" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccelerometer)
Provides:       crate(%{pkgname}/uifocusanimationcoordinator)
Provides:       crate(%{pkgname}/uipagecontrolprogress)
Provides:       crate(%{pkgname}/uipencilinteraction)
Provides:       crate(%{pkgname}/uiupdateinfo)

%description -n %{name}+uiaccelerometer
This metapackage enables feature "UIAccelerometer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFocusAnimationCoordinator", "UIPageControlProgress", "UIPencilInteraction", and "UIUpdateInfo" features.

%package     -n %{name}+uiaccessibility
Summary:        Bindings to the UIKit framework - feature "UIAccessibility"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibility)

%description -n %{name}+uiaccessibility
This metapackage enables feature "UIAccessibility" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccessibilityadditions
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityAdditions" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityadditions)
Provides:       crate(%{pkgname}/uiaccessibilitycustomrotor)

%description -n %{name}+uiaccessibilityadditions
This metapackage enables feature "UIAccessibilityAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityCustomRotor" feature.

%package     -n %{name}+uiaccessibilityconstants
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityConstants"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityconstants)

%description -n %{name}+uiaccessibilityconstants
This metapackage enables feature "UIAccessibilityConstants" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiaccessibilitycontainer
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityContainer" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilitycontainer)
Provides:       crate(%{pkgname}/uiprintpagerenderer)

%description -n %{name}+uiaccessibilitycontainer
This metapackage enables feature "UIAccessibilityContainer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrintPageRenderer" feature.

%package     -n %{name}+uiaccessibilitycustomaction
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityCustomAction" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilitycustomaction)
Provides:       crate(%{pkgname}/uiaccessibilitylocationdescriptor)
Provides:       crate(%{pkgname}/uisearchsuggestion)

%description -n %{name}+uiaccessibilitycustomaction
This metapackage enables feature "UIAccessibilityCustomAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityLocationDescriptor", and "UISearchSuggestion" features.

%package     -n %{name}+uiaccessibilityelement
Summary:        Bindings to the UIKit framework - feature "UIAccessibilityElement" and 17 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaccessibilityelement)
Provides:       crate(%{pkgname}/uiaccessibilityidentification)
Provides:       crate(%{pkgname}/uiactivityitemsconfigurationreading-sharesheet)
Provides:       crate(%{pkgname}/uicontextualaction)
Provides:       crate(%{pkgname}/uidocumentviewcontrollerlaunchoptions)
Provides:       crate(%{pkgname}/uifindsession)
Provides:       crate(%{pkgname}/uifontmetrics)
Provides:       crate(%{pkgname}/uimenuleaf)
Provides:       crate(%{pkgname}/uinibloading)
Provides:       crate(%{pkgname}/uisearchdisplaycontroller)
Provides:       crate(%{pkgname}/uisearchtab)
Provides:       crate(%{pkgname}/uismartreplysuggestion)
Provides:       crate(%{pkgname}/uistoryboardpopoversegue)
Provides:       crate(%{pkgname}/uistoryboardsegue)
Provides:       crate(%{pkgname}/uistringdrawing)
Provides:       crate(%{pkgname}/uitab)
Provides:       crate(%{pkgname}/uitooltipinteraction)
Provides:       crate(%{pkgname}/uitrait)

%description -n %{name}+uiaccessibilityelement
This metapackage enables feature "UIAccessibilityElement" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAccessibilityIdentification", "UIActivityItemsConfigurationReading_ShareSheet", "UIContextualAction", "UIDocumentViewControllerLaunchOptions", "UIFindSession", "UIFontMetrics", "UIMenuLeaf", "UINibLoading", "UISearchDisplayController", "UISearchTab", "UISmartReplySuggestion", "UIStoryboardPopoverSegue", "UIStoryboardSegue", "UIStringDrawing", "UITab", "UIToolTipInteraction", and "UITrait" features.

%package     -n %{name}+uiaction
Summary:        Bindings to the UIKit framework - feature "UIAction" and 9 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiaction)
Provides:       crate(%{pkgname}/uiactionsheet)
Provides:       crate(%{pkgname}/uialertview)
Provides:       crate(%{pkgname}/uicollectionviewcell)
Provides:       crate(%{pkgname}/uicollectionviewtransitionlayout)
Provides:       crate(%{pkgname}/uicolorwell)
Provides:       crate(%{pkgname}/uicontentunavailableconfigurationstate)
Provides:       crate(%{pkgname}/uiswitch)
Provides:       crate(%{pkgname}/uitableviewheaderfooterview)
Provides:       crate(%{pkgname}/uiwindowsceneactivationaction)

%description -n %{name}+uiaction
This metapackage enables feature "UIAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActionSheet", "UIAlertView", "UICollectionViewCell", "UICollectionViewTransitionLayout", "UIColorWell", "UIContentUnavailableConfigurationState", "UISwitch", "UITableViewHeaderFooterView", and "UIWindowSceneActivationAction" features.

%package     -n %{name}+uiactivity
Summary:        Bindings to the UIKit framework - feature "UIActivity" and 5 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivity)
Provides:       crate(%{pkgname}/uifindinteraction)
Provides:       crate(%{pkgname}/uilocalizedindexedcollation)
Provides:       crate(%{pkgname}/uimenubuilder)
Provides:       crate(%{pkgname}/uisheetpresentationcontroller)
Provides:       crate(%{pkgname}/uitabgroup)

%description -n %{name}+uiactivity
This metapackage enables feature "UIActivity" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFindInteraction", "UILocalizedIndexedCollation", "UIMenuBuilder", "UISheetPresentationController", and "UITabGroup" features.

%package     -n %{name}+uiactivitycollaborationmoderestriction
Summary:        Bindings to the UIKit framework - feature "UIActivityCollaborationModeRestriction" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivitycollaborationmoderestriction)
Provides:       crate(%{pkgname}/uieventattribution)

%description -n %{name}+uiactivitycollaborationmoderestriction
This metapackage enables feature "UIActivityCollaborationModeRestriction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIEventAttribution" feature.

%package     -n %{name}+uiactivityitemprovider
Summary:        Bindings to the UIKit framework - feature "UIActivityItemProvider"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsoperation) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityitemprovider)

%description -n %{name}+uiactivityitemprovider
This metapackage enables feature "UIActivityItemProvider" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiactivityitemsconfiguration
Summary:        Bindings to the UIKit framework - feature "UIActivityItemsConfiguration" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityitemsconfiguration)
Provides:       crate(%{pkgname}/uiactivityitemsconfigurationreading)

%description -n %{name}+uiactivityitemsconfiguration
This metapackage enables feature "UIActivityItemsConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIActivityItemsConfigurationReading" feature.

%package     -n %{name}+uiactivityviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIActivityViewController"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiactivityviewcontroller)

%description -n %{name}+uiactivityviewcontroller
This metapackage enables feature "UIActivityViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uialertcontroller
Summary:        Bindings to the UIKit framework - feature "UIAlertController" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uialertcontroller)
Provides:       crate(%{pkgname}/uinavigationcontroller)
Provides:       crate(%{pkgname}/uisearchcontroller)
Provides:       crate(%{pkgname}/uisplitviewcontroller)

%description -n %{name}+uialertcontroller
This metapackage enables feature "UIAlertController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UINavigationController", "UISearchController", and "UISplitViewController" features.

%package     -n %{name}+uiappearance
Summary:        Bindings to the UIKit framework - feature "UIAppearance" and 14 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/uiappearance)
Provides:       crate(%{pkgname}/uiattachmentbehavior)
Provides:       crate(%{pkgname}/uidraginteraction)
Provides:       crate(%{pkgname}/uidynamicbehavior)
Provides:       crate(%{pkgname}/uidynamicitembehavior)
Provides:       crate(%{pkgname}/uigravitybehavior)
Provides:       crate(%{pkgname}/uiinteraction)
Provides:       crate(%{pkgname}/uipopovercontroller)
Provides:       crate(%{pkgname}/uipopoverpresentationcontroller)
Provides:       crate(%{pkgname}/uiprintpaper)
Provides:       crate(%{pkgname}/uipushbehavior)
Provides:       crate(%{pkgname}/uiswipeactionsconfiguration)
Provides:       crate(%{pkgname}/uitextinteraction)
Provides:       crate(%{pkgname}/uitextselectiondisplayinteraction)
Provides:       crate(%{pkgname}/uitextselectionhighlightview)

%description -n %{name}+uiappearance
This metapackage enables feature "UIAppearance" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIAttachmentBehavior", "UIDragInteraction", "UIDynamicBehavior", "UIDynamicItemBehavior", "UIGravityBehavior", "UIInteraction", "UIPopoverController", "UIPopoverPresentationController", "UIPrintPaper", "UIPushBehavior", "UISwipeActionsConfiguration", "UITextInteraction", "UITextSelectionDisplayInteraction", and "UITextSelectionHighlightView" features.

%package     -n %{name}+uiapplication
Summary:        Bindings to the UIKit framework - feature "UIApplication"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiapplication)

%description -n %{name}+uiapplication
This metapackage enables feature "UIApplication" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiapplicationshortcutitem
Summary:        Bindings to the UIKit framework - feature "UIApplicationShortcutItem"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiapplicationshortcutitem)

%description -n %{name}+uiapplicationshortcutitem
This metapackage enables feature "UIApplicationShortcutItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uibackgroundconfiguration
Summary:        Bindings to the UIKit framework - feature "UIBackgroundConfiguration" and 42 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uibackgroundconfiguration)
Provides:       crate(%{pkgname}/uiblureffect)
Provides:       crate(%{pkgname}/uicontentconfiguration)
Provides:       crate(%{pkgname}/uicontentunavailablebuttonproperties)
Provides:       crate(%{pkgname}/uicontentunavailableimageproperties)
Provides:       crate(%{pkgname}/uicontentunavailabletextproperties)
Provides:       crate(%{pkgname}/uicontextmenuinteraction)
Provides:       crate(%{pkgname}/uicornerconfiguration)
Provides:       crate(%{pkgname}/uicornerradius)
Provides:       crate(%{pkgname}/uidragpreview)
Provides:       crate(%{pkgname}/uifocuseffect)
Provides:       crate(%{pkgname}/uifocusmovementhint)
Provides:       crate(%{pkgname}/uiglasseffect)
Provides:       crate(%{pkgname}/uigraphicsrenderer)
Provides:       crate(%{pkgname}/uihovereffect)
Provides:       crate(%{pkgname}/uihovereffectlayer)
Provides:       crate(%{pkgname}/uihoverstyle)
Provides:       crate(%{pkgname}/uikeyboardlayoutguide)
Provides:       crate(%{pkgname}/uilistcontentimageproperties)
Provides:       crate(%{pkgname}/uilistcontenttextproperties)
Provides:       crate(%{pkgname}/uilistseparatorconfiguration)
Provides:       crate(%{pkgname}/uimainmenusystem)
Provides:       crate(%{pkgname}/uimenudisplaypreferences)
Provides:       crate(%{pkgname}/uipointeraccessory)
Provides:       crate(%{pkgname}/uipointerregion)
Provides:       crate(%{pkgname}/uiregion)
Provides:       crate(%{pkgname}/uiscenedestructioncondition)
Provides:       crate(%{pkgname}/uishadowproperties)
Provides:       crate(%{pkgname}/uishape)
Provides:       crate(%{pkgname}/uisymbolcontenttransition)
Provides:       crate(%{pkgname}/uitargeteddragpreview)
Provides:       crate(%{pkgname}/uitargetedpreview)
Provides:       crate(%{pkgname}/uitextdropproposal)
Provides:       crate(%{pkgname}/uitimingcurveprovider)
Provides:       crate(%{pkgname}/uivibrancyeffect)
Provides:       crate(%{pkgname}/uivisualeffect)
Provides:       crate(%{pkgname}/uiwindowscenegeometry)
Provides:       crate(%{pkgname}/uiwindowsceneplacement)
Provides:       crate(%{pkgname}/uiwindowsceneprominentplacement)
Provides:       crate(%{pkgname}/uiwindowscenepushplacement)
Provides:       crate(%{pkgname}/uiwindowscenereplaceplacement)
Provides:       crate(%{pkgname}/uiwindowscenestandardplacement)
Provides:       crate(%{pkgname}/uizoomtransitionoptions)

%description -n %{name}+uibackgroundconfiguration
This metapackage enables feature "UIBackgroundConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIBlurEffect", "UIContentConfiguration", "UIContentUnavailableButtonProperties", "UIContentUnavailableImageProperties", "UIContentUnavailableTextProperties", "UIContextMenuInteraction", "UICornerConfiguration", "UICornerRadius", "UIDragPreview", "UIFocusEffect", "UIFocusMovementHint", "UIGlassEffect", "UIGraphicsRenderer", "UIHoverEffect", "UIHoverEffectLayer", "UIHoverStyle", "UIKeyboardLayoutGuide", "UIListContentImageProperties", "UIListContentTextProperties", "UIListSeparatorConfiguration", "UIMainMenuSystem", "UIMenuDisplayPreferences", "UIPointerAccessory", "UIPointerRegion", "UIRegion", "UISceneDestructionCondition", "UIShadowProperties", "UIShape", "UISymbolContentTransition", "UITargetedDragPreview", "UITargetedPreview", "UITextDropProposal", "UITimingCurveProvider", "UIVibrancyEffect", "UIVisualEffect", "UIWindowSceneGeometry", "UIWindowScenePlacement", "UIWindowSceneProminentPlacement", "UIWindowScenePushPlacement", "UIWindowSceneReplacePlacement", "UIWindowSceneStandardPlacement", and "UIZoomTransitionOptions" features.

%package     -n %{name}+uibarbuttonitem
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItem"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitem)

%description -n %{name}+uibarbuttonitem
This metapackage enables feature "UIBarButtonItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uibarbuttonitemappearance
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemAppearance" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitemappearance)
Provides:       crate(%{pkgname}/uibaritem)
Provides:       crate(%{pkgname}/uinavigationbarappearance)
Provides:       crate(%{pkgname}/uitabbarappearance)
Provides:       crate(%{pkgname}/uitabbaritem)

%description -n %{name}+uibarbuttonitemappearance
This metapackage enables feature "UIBarButtonItemAppearance" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIBarItem", "UINavigationBarAppearance", "UITabBarAppearance", and "UITabBarItem" features.

%package     -n %{name}+uibarbuttonitembadge
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemBadge" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitembadge)
Provides:       crate(%{pkgname}/uiconfigurationstate)
Provides:       crate(%{pkgname}/uikey)
Provides:       crate(%{pkgname}/uilayoutguide)
Provides:       crate(%{pkgname}/uisceneconfiguration)

%description -n %{name}+uibarbuttonitembadge
This metapackage enables feature "UIBarButtonItemBadge" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIConfigurationState", "UIKey", "UILayoutGuide", and "UISceneConfiguration" features.

%package     -n %{name}+uibarbuttonitemgroup
Summary:        Bindings to the UIKit framework - feature "UIBarButtonItemGroup" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibarbuttonitemgroup)
Provides:       crate(%{pkgname}/uicellaccessory)
Provides:       crate(%{pkgname}/uideferredmenuelement)
Provides:       crate(%{pkgname}/uikeycommand)
Provides:       crate(%{pkgname}/uitraitcollection)

%description -n %{name}+uibarbuttonitemgroup
This metapackage enables feature "UIBarButtonItemGroup" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICellAccessory", "UIDeferredMenuElement", "UIKeyCommand", and "UITraitCollection" features.

%package     -n %{name}+uibutton
Summary:        Bindings to the UIKit framework - feature "UIButton" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibutton)
Provides:       crate(%{pkgname}/uilabel)
Provides:       crate(%{pkgname}/uilistcontentconfiguration)
Provides:       crate(%{pkgname}/uipickerview)

%description -n %{name}+uibutton
This metapackage enables feature "UIButton" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UILabel", "UIListContentConfiguration", and "UIPickerView" features.

%package     -n %{name}+uibuttonconfiguration
Summary:        Bindings to the UIKit framework - feature "UIButtonConfiguration" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uibuttonconfiguration)
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerformattingstyle)

%description -n %{name}+uibuttonconfiguration
This metapackage enables feature "UIButtonConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UITextFormattingViewControllerFormattingStyle" feature.

%package     -n %{name}+uicalendarselectionmultidate
Summary:        Bindings to the UIKit framework - feature "UICalendarSelectionMultiDate"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarselectionmultidate)

%description -n %{name}+uicalendarselectionmultidate
This metapackage enables feature "UICalendarSelectionMultiDate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicalendarselectionsingledate
Summary:        Bindings to the UIKit framework - feature "UICalendarSelectionSingleDate" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarselectionsingledate)
Provides:       crate(%{pkgname}/uicalendarselectionweekofyear)

%description -n %{name}+uicalendarselectionsingledate
This metapackage enables feature "UICalendarSelectionSingleDate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UICalendarSelectionWeekOfYear" feature.

%package     -n %{name}+uicalendarview
Summary:        Bindings to the UIKit framework - feature "UICalendarView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdateinterval) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uicalendarview)

%description -n %{name}+uicalendarview
This metapackage enables feature "UICalendarView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicloudsharingcontroller
Summary:        Bindings to the UIKit framework - feature "UICloudSharingController"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicloudsharingcontroller)

%description -n %{name}+uicloudsharingcontroller
This metapackage enables feature "UICloudSharingController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionlayoutlist
Summary:        Bindings to the UIKit framework - feature "UICollectionLayoutList"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionlayoutlist)

%description -n %{name}+uicollectionlayoutlist
This metapackage enables feature "UICollectionLayoutList" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionview
Summary:        Bindings to the UIKit framework - feature "UICollectionView"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionview)

%description -n %{name}+uicollectionview
This metapackage enables feature "UICollectionView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewcompositionallayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewCompositionalLayout"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewcompositionallayout)

%description -n %{name}+uicollectionviewcompositionallayout
This metapackage enables feature "UICollectionViewCompositionalLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewcontroller
Summary:        Bindings to the UIKit framework - feature "UICollectionViewController" and 7 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewcontroller)
Provides:       crate(%{pkgname}/uicolorpickerviewcontroller)
Provides:       crate(%{pkgname}/uidocumentviewcontroller)
Provides:       crate(%{pkgname}/uifontpickerviewcontroller)
Provides:       crate(%{pkgname}/uireferencelibraryviewcontroller)
Provides:       crate(%{pkgname}/uisearchcontainerviewcontroller)
Provides:       crate(%{pkgname}/uitableviewcontroller)
Provides:       crate(%{pkgname}/uitextformattingviewcontroller)

%description -n %{name}+uicollectionviewcontroller
This metapackage enables feature "UICollectionViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIColorPickerViewController", "UIDocumentViewController", "UIFontPickerViewController", "UIReferenceLibraryViewController", "UISearchContainerViewController", "UITableViewController", and "UITextFormattingViewController" features.

%package     -n %{name}+uicollectionviewflowlayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewFlowLayout"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewflowlayout)

%description -n %{name}+uicollectionviewflowlayout
This metapackage enables feature "UICollectionViewFlowLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewitemregistration
Summary:        Bindings to the UIKit framework - feature "UICollectionViewItemRegistration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewitemregistration)

%description -n %{name}+uicollectionviewitemregistration
This metapackage enables feature "UICollectionViewItemRegistration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollectionviewlayout
Summary:        Bindings to the UIKit framework - feature "UICollectionViewLayout"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicollectionviewlayout)

%description -n %{name}+uicollectionviewlayout
This metapackage enables feature "UICollectionViewLayout" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicollisionbehavior
Summary:        Bindings to the UIKit framework - feature "UICollisionBehavior"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uicollisionbehavior)

%description -n %{name}+uicollisionbehavior
This metapackage enables feature "UICollisionBehavior" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicolor
Summary:        Bindings to the UIKit framework - feature "UIColor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicolor)

%description -n %{name}+uicolor
This metapackage enables feature "UIColor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicommand
Summary:        Bindings to the UIKit framework - feature "UICommand" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicommand)
Provides:       crate(%{pkgname}/uimenu)

%description -n %{name}+uicommand
This metapackage enables feature "UICommand" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMenu" feature.

%package     -n %{name}+uicontentsizecategory
Summary:        Bindings to the UIKit framework - feature "UIContentSizeCategory"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontentsizecategory)

%description -n %{name}+uicontentsizecategory
This metapackage enables feature "UIContentSizeCategory" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicontentunavailableconfiguration
Summary:        Bindings to the UIKit framework - feature "UIContentUnavailableConfiguration" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontentunavailableconfiguration)
Provides:       crate(%{pkgname}/uiprintformatter)

%description -n %{name}+uicontentunavailableconfiguration
This metapackage enables feature "UIContentUnavailableConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrintFormatter" feature.

%package     -n %{name}+uicontextmenuconfiguration
Summary:        Bindings to the UIKit framework - feature "UIContextMenuConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uicontextmenuconfiguration)

%description -n %{name}+uicontextmenuconfiguration
This metapackage enables feature "UIContextMenuConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uicontrol
Summary:        Bindings to the UIKit framework - feature "UIControl"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uicontrol)

%description -n %{name}+uicontrol
This metapackage enables feature "UIControl" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiconversationcontext
Summary:        Bindings to the UIKit framework - feature "UIConversationContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspersonnamecomponents) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiconversationcontext)

%description -n %{name}+uiconversationcontext
This metapackage enables feature "UIConversationContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiconversationentry
Summary:        Bindings to the UIKit framework - feature "UIConversationEntry"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiconversationentry)

%description -n %{name}+uiconversationentry
This metapackage enables feature "UIConversationEntry" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidatepicker
Summary:        Bindings to the UIKit framework - feature "UIDatePicker"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uidatepicker)

%description -n %{name}+uidatepicker
This metapackage enables feature "UIDatePicker" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidevice
Summary:        Bindings to the UIKit framework - feature "UIDevice"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uidevice)

%description -n %{name}+uidevice
This metapackage enables feature "UIDevice" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidiffabledatasource
Summary:        Bindings to the UIKit framework - feature "UIDiffableDataSource"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsorderedcollectiondifference) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidiffabledatasource)

%description -n %{name}+uidiffabledatasource
This metapackage enables feature "UIDiffableDataSource" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocument
Summary:        Bindings to the UIKit framework - feature "UIDocument"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilepresenter) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsundomanager) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uidocument)

%description -n %{name}+uidocument
This metapackage enables feature "UIDocument" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentbrowseraction
Summary:        Bindings to the UIKit framework - feature "UIDocumentBrowserAction"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentbrowseraction)

%description -n %{name}+uidocumentbrowseraction
This metapackage enables feature "UIDocumentBrowserAction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentbrowserviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentBrowserViewController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentbrowserviewcontroller)

%description -n %{name}+uidocumentbrowserviewcontroller
This metapackage enables feature "UIDocumentBrowserViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentinteractioncontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentInteractionController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentinteractioncontroller)

%description -n %{name}+uidocumentinteractioncontroller
This metapackage enables feature "UIDocumentInteractionController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidocumentmenuviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIDocumentMenuViewController" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentmenuviewcontroller)
Provides:       crate(%{pkgname}/uidocumentpickerextensionviewcontroller)
Provides:       crate(%{pkgname}/uidocumentpickerviewcontroller)

%description -n %{name}+uidocumentmenuviewcontroller
This metapackage enables feature "UIDocumentMenuViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIDocumentPickerExtensionViewController", and "UIDocumentPickerViewController" features.

%package     -n %{name}+uidocumentproperties
Summary:        Bindings to the UIKit framework - feature "UIDocumentProperties"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uidocumentproperties)

%description -n %{name}+uidocumentproperties
This metapackage enables feature "UIDocumentProperties" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidragitem
Summary:        Bindings to the UIKit framework - feature "UIDragItem"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Provides:       crate(%{pkgname}/uidragitem)

%description -n %{name}+uidragitem
This metapackage enables feature "UIDragItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidragpreviewparameters
Summary:        Bindings to the UIKit framework - feature "UIDragPreviewParameters" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uidragpreviewparameters)
Provides:       crate(%{pkgname}/uipreviewparameters)

%description -n %{name}+uidragpreviewparameters
This metapackage enables feature "UIDragPreviewParameters" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPreviewParameters" feature.

%package     -n %{name}+uidragsession
Summary:        Bindings to the UIKit framework - feature "UIDragSession"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidragsession)

%description -n %{name}+uidragsession
This metapackage enables feature "UIDragSession" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidropinteraction
Summary:        Bindings to the UIKit framework - feature "UIDropInteraction"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uidropinteraction)

%description -n %{name}+uidropinteraction
This metapackage enables feature "UIDropInteraction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uidynamicanimator
Summary:        Bindings to the UIKit framework - feature "UIDynamicAnimator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uidynamicanimator)

%description -n %{name}+uidynamicanimator
This metapackage enables feature "UIDynamicAnimator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uieditmenuinteraction
Summary:        Bindings to the UIKit framework - feature "UIEditMenuInteraction" and 6 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uieditmenuinteraction)
Provides:       crate(%{pkgname}/uifocusguide)
Provides:       crate(%{pkgname}/uiindirectscribbleinteraction)
Provides:       crate(%{pkgname}/uipointerstyle)
Provides:       crate(%{pkgname}/uitabsidebaritem)
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerconfiguration)
Provides:       crate(%{pkgname}/uitrackinglayoutguide)

%description -n %{name}+uieditmenuinteraction
This metapackage enables feature "UIEditMenuInteraction" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIFocusGuide", "UIIndirectScribbleInteraction", "UIPointerStyle", "UITabSidebarItem", "UITextFormattingViewControllerConfiguration", and "UITrackingLayoutGuide" features.

%package     -n %{name}+uievent
Summary:        Bindings to the UIKit framework - feature "UIEvent"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uievent)

%description -n %{name}+uievent
This metapackage enables feature "UIEvent" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uifieldbehavior
Summary:        Bindings to the UIKit framework - feature "UIFieldBehavior" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uifieldbehavior)
Provides:       crate(%{pkgname}/uipress)

%description -n %{name}+uifieldbehavior
This metapackage enables feature "UIFieldBehavior" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPress" feature.

%package     -n %{name}+uifocus
Summary:        Bindings to the UIKit framework - feature "UIFocus"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifocus)

%description -n %{name}+uifocus
This metapackage enables feature "UIFocus" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uifocussystem-uikitadditions
Summary:        Bindings to the UIKit framework - feature "UIFocusSystem_UIKitAdditions" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uifocussystem-uikitadditions)
Provides:       crate(%{pkgname}/uitextdragurlpreviews)

%description -n %{name}+uifocussystem-uikitadditions
This metapackage enables feature "UIFocusSystem_UIKitAdditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UITextDragURLPreviews" feature.

%package     -n %{name}+uifontdescriptor
Summary:        Bindings to the UIKit framework - feature "UIFontDescriptor" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifontdescriptor)
Provides:       crate(%{pkgname}/uiusernotificationsettings)

%description -n %{name}+uifontdescriptor
This metapackage enables feature "UIFontDescriptor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIUserNotificationSettings" feature.

%package     -n %{name}+uifontpickerviewcontrollerconfiguration
Summary:        Bindings to the UIKit framework - feature "UIFontPickerViewControllerConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uifontpickerviewcontrollerconfiguration)

%description -n %{name}+uifontpickerviewcontrollerconfiguration
This metapackage enables feature "UIFontPickerViewControllerConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigeometry
Summary:        Bindings to the UIKit framework - feature "UIGeometry"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uigeometry)

%description -n %{name}+uigeometry
This metapackage enables feature "UIGeometry" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIGestureRecognizer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uigesturerecognizer)

%description -n %{name}+uigesturerecognizer
This metapackage enables feature "UIGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigesturerecognizersubclass
Summary:        Bindings to the UIKit framework - feature "UIGestureRecognizerSubclass" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uigesturerecognizersubclass)
Provides:       crate(%{pkgname}/uipressesevent)

%description -n %{name}+uigesturerecognizersubclass
This metapackage enables feature "UIGestureRecognizerSubclass" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPressesEvent" feature.

%package     -n %{name}+uigraphics
Summary:        Bindings to the UIKit framework - feature "UIGraphics"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphics)

%description -n %{name}+uigraphics
This metapackage enables feature "UIGraphics" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicsimagerenderer
Summary:        Bindings to the UIKit framework - feature "UIGraphicsImageRenderer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicsimagerenderer)

%description -n %{name}+uigraphicsimagerenderer
This metapackage enables feature "UIGraphicsImageRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicspdfrenderer
Summary:        Bindings to the UIKit framework - feature "UIGraphicsPDFRenderer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicspdfrenderer)

%description -n %{name}+uigraphicspdfrenderer
This metapackage enables feature "UIGraphicsPDFRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uigraphicsrenderersubclass
Summary:        Bindings to the UIKit framework - feature "UIGraphicsRendererSubclass" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/uigraphicsrenderersubclass)
Provides:       crate(%{pkgname}/uiprinterpickercontroller)
Provides:       crate(%{pkgname}/uiwindowsceneactivationinteraction)

%description -n %{name}+uigraphicsrenderersubclass
This metapackage enables feature "UIGraphicsRendererSubclass" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPrinterPickerController", and "UIWindowSceneActivationInteraction" features.

%package     -n %{name}+uiguidedaccess
Summary:        Bindings to the UIKit framework - feature "UIGuidedAccess"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiguidedaccess)

%description -n %{name}+uiguidedaccess
This metapackage enables feature "UIGuidedAccess" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uihovergesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIHoverGestureRecognizer" and 4 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Provides:       crate(%{pkgname}/uihovergesturerecognizer)
Provides:       crate(%{pkgname}/uipinchgesturerecognizer)
Provides:       crate(%{pkgname}/uirotationgesturerecognizer)
Provides:       crate(%{pkgname}/uiscreenedgepangesturerecognizer)
Provides:       crate(%{pkgname}/uitapgesturerecognizer)

%description -n %{name}+uihovergesturerecognizer
This metapackage enables feature "UIHoverGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPinchGestureRecognizer", "UIRotationGestureRecognizer", "UIScreenEdgePanGestureRecognizer", and "UITapGestureRecognizer" features.

%package     -n %{name}+uiimage
Summary:        Bindings to the UIKit framework - feature "UIImage"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiimage)

%description -n %{name}+uiimage
This metapackage enables feature "UIImage" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimageconfiguration
Summary:        Bindings to the UIKit framework - feature "UIImageConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiimageconfiguration)

%description -n %{name}+uiimageconfiguration
This metapackage enables feature "UIImageConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagepickercontroller
Summary:        Bindings to the UIKit framework - feature "UIImagePickerController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagepickercontroller)

%description -n %{name}+uiimagepickercontroller
This metapackage enables feature "UIImagePickerController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagereader
Summary:        Bindings to the UIKit framework - feature "UIImageReader"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagereader)

%description -n %{name}+uiimagereader
This metapackage enables feature "UIImageReader" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimagesymbolconfiguration
Summary:        Bindings to the UIKit framework - feature "UIImageSymbolConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslocale) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiimagesymbolconfiguration)

%description -n %{name}+uiimagesymbolconfiguration
This metapackage enables feature "UIImageSymbolConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiimageview
Summary:        Bindings to the UIKit framework - feature "UIImageView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiimageview)

%description -n %{name}+uiimageview
This metapackage enables feature "UIImageView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiinputviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIInputViewController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uiinputviewcontroller)

%description -n %{name}+uiinputviewcontroller
This metapackage enables feature "UIInputViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uilargecontentviewer
Summary:        Bindings to the UIKit framework - feature "UILargeContentViewer" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uilargecontentviewer)
Provides:       crate(%{pkgname}/uipointerlockstate)
Provides:       crate(%{pkgname}/uiscenesystemprotectionmanager)

%description -n %{name}+uilargecontentviewer
This metapackage enables feature "UILargeContentViewer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIPointerLockState", and "UISceneSystemProtectionManager" features.

%package     -n %{name}+uilocalnotification
Summary:        Bindings to the UIKit framework - feature "UILocalNotification"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscalendar) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nstimezone) >= 0.3.2
Provides:       crate(%{pkgname}/uilocalnotification)

%description -n %{name}+uilocalnotification
This metapackage enables feature "UILocalNotification" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uilongpressgesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UILongPressGestureRecognizer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Provides:       crate(%{pkgname}/uilongpressgesturerecognizer)

%description -n %{name}+uilongpressgesturerecognizer
This metapackage enables feature "UILongPressGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uimailconversationcontext
Summary:        Bindings to the UIKit framework - feature "UIMailConversationContext" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimailconversationcontext)
Provides:       crate(%{pkgname}/uimailconversationentry)

%description -n %{name}+uimailconversationcontext
This metapackage enables feature "UIMailConversationContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIMailConversationEntry" feature.

%package     -n %{name}+uimanageddocument
Summary:        Bindings to the UIKit framework - feature "UIManagedDocument"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsfilepresenter) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uimanageddocument)

%description -n %{name}+uimanageddocument
This metapackage enables feature "UIManagedDocument" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uimenucontroller
Summary:        Bindings to the UIKit framework - feature "UIMenuController" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimenucontroller)
Provides:       crate(%{pkgname}/uiscreen)

%description -n %{name}+uimenucontroller
This metapackage enables feature "UIMenuController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIScreen" feature.

%package     -n %{name}+uimotioneffect
Summary:        Bindings to the UIKit framework - feature "UIMotionEffect"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uimotioneffect)

%description -n %{name}+uimotioneffect
This metapackage enables feature "UIMotionEffect" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uinavigationitem
Summary:        Bindings to the UIKit framework - feature "UINavigationItem"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uinavigationitem)

%description -n %{name}+uinavigationitem
This metapackage enables feature "UINavigationItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uinib
Summary:        Bindings to the UIKit framework - feature "UINib"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uinib)

%description -n %{name}+uinib
This metapackage enables feature "UINib" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiopenurlcontext
Summary:        Bindings to the UIKit framework - feature "UIOpenURLContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiopenurlcontext)

%description -n %{name}+uiopenurlcontext
This metapackage enables feature "UIOpenURLContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipageviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIPageViewController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uipageviewcontroller)

%description -n %{name}+uipageviewcontroller
This metapackage enables feature "UIPageViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipangesturerecognizer
Summary:        Bindings to the UIKit framework - feature "UIPanGestureRecognizer" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Provides:       crate(%{pkgname}/uipangesturerecognizer)
Provides:       crate(%{pkgname}/uiswipegesturerecognizer)

%description -n %{name}+uipangesturerecognizer
This metapackage enables feature "UIPanGestureRecognizer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UISwipeGestureRecognizer" feature.

%package     -n %{name}+uipasteconfiguration
Summary:        Bindings to the UIKit framework - feature "UIPasteConfiguration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteconfiguration)

%description -n %{name}+uipasteconfiguration
This metapackage enables feature "UIPasteConfiguration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipasteconfigurationsupporting
Summary:        Bindings to the UIKit framework - feature "UIPasteConfigurationSupporting"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteconfigurationsupporting)

%description -n %{name}+uipasteconfigurationsupporting
This metapackage enables feature "UIPasteConfigurationSupporting" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uipasteboard
Summary:        Bindings to the UIKit framework - feature "UIPasteboard"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uipasteboard)

%description -n %{name}+uipasteboard
This metapackage enables feature "UIPasteboard" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprinterror
Summary:        Bindings to the UIKit framework - feature "UIPrintError" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiprinterror)
Provides:       crate(%{pkgname}/uiscenedefinitions)

%description -n %{name}+uiprinterror
This metapackage enables feature "UIPrintError" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UISceneDefinitions" feature.

%package     -n %{name}+uiprintinfo
Summary:        Bindings to the UIKit framework - feature "UIPrintInfo"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintinfo)

%description -n %{name}+uiprintinfo
This metapackage enables feature "UIPrintInfo" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprintinteractioncontroller
Summary:        Bindings to the UIKit framework - feature "UIPrintInteractionController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintinteractioncontroller)

%description -n %{name}+uiprintinteractioncontroller
This metapackage enables feature "UIPrintInteractionController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprintserviceextension
Summary:        Bindings to the UIKit framework - feature "UIPrintServiceExtension"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprintserviceextension)

%description -n %{name}+uiprintserviceextension
This metapackage enables feature "UIPrintServiceExtension" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprinter
Summary:        Bindings to the UIKit framework - feature "UIPrinter"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uiprinter)

%description -n %{name}+uiprinter
This metapackage enables feature "UIPrinter" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiprogressview
Summary:        Bindings to the UIKit framework - feature "UIProgressView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uiprogressview)

%description -n %{name}+uiprogressview
This metapackage enables feature "UIProgressView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uirefreshcontrol
Summary:        Bindings to the UIKit framework - feature "UIRefreshControl"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uirefreshcontrol)

%description -n %{name}+uirefreshcontrol
This metapackage enables feature "UIRefreshControl" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiresponder
Summary:        Bindings to the UIKit framework - feature "UIResponder"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsundomanager) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiresponder)

%description -n %{name}+uiresponder
This metapackage enables feature "UIResponder" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscene
Summary:        Bindings to the UIKit framework - feature "UIScene"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscene)

%description -n %{name}+uiscene
This metapackage enables feature "UIScene" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisceneactivationconditions
Summary:        Bindings to the UIKit framework - feature "UISceneActivationConditions"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uisceneactivationconditions)

%description -n %{name}+uisceneactivationconditions
This metapackage enables feature "UISceneActivationConditions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisceneoptions
Summary:        Bindings to the UIKit framework - feature "UISceneOptions"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uisceneoptions)

%description -n %{name}+uisceneoptions
This metapackage enables feature "UISceneOptions" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscenesession
Summary:        Bindings to the UIKit framework - feature "UISceneSession"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/uisceneconfiguration)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscenesession)

%description -n %{name}+uiscenesession
This metapackage enables feature "UISceneSession" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscenesessionactivationrequest
Summary:        Bindings to the UIKit framework - feature "UISceneSessionActivationRequest"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiscenesessionactivationrequest)

%description -n %{name}+uiscenesessionactivationrequest
This metapackage enables feature "UISceneSessionActivationRequest" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscreenshotservice
Summary:        Bindings to the UIKit framework - feature "UIScreenshotService"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Provides:       crate(%{pkgname}/uiscreenshotservice)

%description -n %{name}+uiscreenshotservice
This metapackage enables feature "UIScreenshotService" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiscrollview
Summary:        Bindings to the UIKit framework - feature "UIScrollView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/uiscrollview)

%description -n %{name}+uiscrollview
This metapackage enables feature "UIScrollView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisearchbar
Summary:        Bindings to the UIKit framework - feature "UISearchBar"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uisearchbar)

%description -n %{name}+uisearchbar
This metapackage enables feature "UISearchBar" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uisearchtextfield
Summary:        Bindings to the UIKit framework - feature "UISearchTextField"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uisearchtextfield)

%description -n %{name}+uisearchtextfield
This metapackage enables feature "UISearchTextField" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uistaterestoration
Summary:        Bindings to the UIKit framework - feature "UIStateRestoration"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uistaterestoration)

%description -n %{name}+uistaterestoration
This metapackage enables feature "UIStateRestoration" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uistoryboard
Summary:        Bindings to the UIKit framework - feature "UIStoryboard"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uistoryboard)

%description -n %{name}+uistoryboard
This metapackage enables feature "UIStoryboard" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitabbarcontroller
Summary:        Bindings to the UIKit framework - feature "UITabBarController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitabbarcontroller)

%description -n %{name}+uitabbarcontroller
This metapackage enables feature "UITabBarController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitabbarcontrollersidebar
Summary:        Bindings to the UIKit framework - feature "UITabBarControllerSidebar"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uitabbarcontrollersidebar)

%description -n %{name}+uitabbarcontrollersidebar
This metapackage enables feature "UITabBarControllerSidebar" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitableview
Summary:        Bindings to the UIKit framework - feature "UITableView"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitableview)

%description -n %{name}+uitableview
This metapackage enables feature "UITableView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextchecker
Summary:        Bindings to the UIKit framework - feature "UITextChecker"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextchecker)

%description -n %{name}+uitextchecker
This metapackage enables feature "UITextChecker" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdragpreviewrenderer
Summary:        Bindings to the UIKit framework - feature "UITextDragPreviewRenderer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdragpreviewrenderer)

%description -n %{name}+uitextdragpreviewrenderer
This metapackage enables feature "UITextDragPreviewRenderer" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdragging
Summary:        Bindings to the UIKit framework - feature "UITextDragging"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdragging)

%description -n %{name}+uitextdragging
This metapackage enables feature "UITextDragging" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextdropping
Summary:        Bindings to the UIKit framework - feature "UITextDropping"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/uitextdropping)

%description -n %{name}+uitextdropping
This metapackage enables feature "UITextDropping" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextfield
Summary:        Bindings to the UIKit framework - feature "UITextField"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextfield)

%description -n %{name}+uitextfield
This metapackage enables feature "UITextField" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingcoordinator
Summary:        Bindings to the UIKit framework - feature "UITextFormattingCoordinator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingcoordinator)

%description -n %{name}+uitextformattingcoordinator
This metapackage enables feature "UITextFormattingCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingviewcontrollerchangevalue
Summary:        Bindings to the UIKit framework - feature "UITextFormattingViewControllerChangeValue"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerchangevalue)

%description -n %{name}+uitextformattingviewcontrollerchangevalue
This metapackage enables feature "UITextFormattingViewControllerChangeValue" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextformattingviewcontrollerformattingdescriptor
Summary:        Bindings to the UIKit framework - feature "UITextFormattingViewControllerFormattingDescriptor"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextformattingviewcontrollerformattingdescriptor)

%description -n %{name}+uitextformattingviewcontrollerformattingdescriptor
This metapackage enables feature "UITextFormattingViewControllerFormattingDescriptor" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextinput
Summary:        Bindings to the UIKit framework - feature "UITextInput"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextinput)

%description -n %{name}+uitextinput
This metapackage enables feature "UITextInput" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextinputtraits
Summary:        Bindings to the UIKit framework - feature "UITextInputTraits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextinputtraits)

%description -n %{name}+uitextinputtraits
This metapackage enables feature "UITextInputTraits" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextitem
Summary:        Bindings to the UIKit framework - feature "UITextItem"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/uitextitem)

%description -n %{name}+uitextitem
This metapackage enables feature "UITextItem" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextpastedelegate
Summary:        Bindings to the UIKit framework - feature "UITextPasteDelegate"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsitemprovider) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextpastedelegate)

%description -n %{name}+uitextpastedelegate
This metapackage enables feature "UITextPasteDelegate" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextsearching
Summary:        Bindings to the UIKit framework - feature "UITextSearching"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsorderedset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uitextsearching)

%description -n %{name}+uitextsearching
This metapackage enables feature "UITextSearching" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitextview
Summary:        Bindings to the UIKit framework - feature "UITextView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitextview)

%description -n %{name}+uitextview
This metapackage enables feature "UITextView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitimingparameters
Summary:        Bindings to the UIKit framework - feature "UITimingParameters"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uitimingparameters)

%description -n %{name}+uitimingparameters
This metapackage enables feature "UITimingParameters" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uitouch
Summary:        Bindings to the UIKit framework - feature "UITouch"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uitouch)

%description -n %{name}+uitouch
This metapackage enables feature "UITouch" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiuseractivity
Summary:        Bindings to the UIKit framework - feature "UIUserActivity" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuseractivity) >= 0.3.2
Provides:       crate(%{pkgname}/uiuseractivity)
Provides:       crate(%{pkgname}/uiwindowsceneactivationconfiguration)

%description -n %{name}+uiuseractivity
This metapackage enables feature "UIUserActivity" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIWindowSceneActivationConfiguration" feature.

%package     -n %{name}+uivideoeditorcontroller
Summary:        Bindings to the UIKit framework - feature "UIVideoEditorController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uivideoeditorcontroller)

%description -n %{name}+uivideoeditorcontroller
This metapackage enables feature "UIVideoEditorController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiview
Summary:        Bindings to the UIKit framework - feature "UIView"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiview)

%description -n %{name}+uiview
This metapackage enables feature "UIView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewanimating
Summary:        Bindings to the UIKit framework - feature "UIViewAnimating" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewanimating)
Provides:       crate(%{pkgname}/uiviewpropertyanimator)

%description -n %{name}+uiviewanimating
This metapackage enables feature "UIViewAnimating" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIViewPropertyAnimator" feature.

%package     -n %{name}+uiviewcontroller
Summary:        Bindings to the UIKit framework - feature "UIViewController"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsextensioncontext) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsextensionrequesthandling) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobjcruntime) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontroller)

%description -n %{name}+uiviewcontroller
This metapackage enables feature "UIViewController" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewcontrollertransitioncoordinator
Summary:        Bindings to the UIKit framework - feature "UIViewControllerTransitionCoordinator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontrollertransitioncoordinator)

%description -n %{name}+uiviewcontrollertransitioncoordinator
This metapackage enables feature "UIViewControllerTransitionCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiviewcontrollertransitioning
Summary:        Bindings to the UIKit framework - feature "UIViewControllerTransitioning"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiviewcontrollertransitioning)

%description -n %{name}+uiviewcontrollertransitioning
This metapackage enables feature "UIViewControllerTransitioning" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwebview
Summary:        Bindings to the UIKit framework - feature "UIWebView"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurlrequest) >= 0.3.2
Provides:       crate(%{pkgname}/uiwebview)

%description -n %{name}+uiwebview
This metapackage enables feature "UIWebView" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwindow
Summary:        Bindings to the UIKit framework - feature "UIWindow"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiwindow)

%description -n %{name}+uiwindow
This metapackage enables feature "UIWindow" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwindowscene
Summary:        Bindings to the UIKit framework - feature "UIWindowScene"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/uiscenesizerestrictions)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/uiwindowscene)

%description -n %{name}+uiwindowscene
This metapackage enables feature "UIWindowScene" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwritingtoolscoordinator
Summary:        Bindings to the UIKit framework - feature "UIWritingToolsCoordinator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/uiwritingtoolscoordinator)

%description -n %{name}+uiwritingtoolscoordinator
This metapackage enables feature "UIWritingToolsCoordinator" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uiwritingtoolscoordinatorcontext
Summary:        Bindings to the UIKit framework - feature "UIWritingToolsCoordinatorContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsattributedstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsrange) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/uiwritingtoolscoordinatorcontext)

%description -n %{name}+uiwritingtoolscoordinatorcontext
This metapackage enables feature "UIWritingToolsCoordinatorContext" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the UIKit framework - feature "bitflags" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname}/bitflags)
Provides:       crate(%{pkgname}/uidatadetectors)
Provides:       crate(%{pkgname}/uiorientation)
Provides:       crate(%{pkgname}/uipopoversupport)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "UIDataDetectors", "UIOrientation", and "UIPopoverSupport" features.

%package     -n %{name}+block2
Summary:        Bindings to the UIKit framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.2
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the UIKit framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/documentmanager)
Requires:       crate(%{pkgname}/nsadaptiveimageglyph)
Requires:       crate(%{pkgname}/nsattributedstring)
Requires:       crate(%{pkgname}/nsdataasset)
Requires:       crate(%{pkgname}/nsdiffabledatasourcesectionsnapshot)
Requires:       crate(%{pkgname}/nsfileproviderextension)
Requires:       crate(%{pkgname}/nsindexpath-uikitadditions)
Requires:       crate(%{pkgname}/nsitemprovider-uikitadditions)
Requires:       crate(%{pkgname}/nslayoutanchor)
Requires:       crate(%{pkgname}/nslayoutconstraint)
Requires:       crate(%{pkgname}/nslayoutmanager)
Requires:       crate(%{pkgname}/nsparagraphstyle)
Requires:       crate(%{pkgname}/nsshadow)
Requires:       crate(%{pkgname}/nsstringdrawing)
Requires:       crate(%{pkgname}/nstext)
Requires:       crate(%{pkgname}/nstextattachment)
Requires:       crate(%{pkgname}/nstextcontainer)
Requires:       crate(%{pkgname}/nstextcontentmanager)
Requires:       crate(%{pkgname}/nstextelement)
Requires:       crate(%{pkgname}/nstextlayoutfragment)
Requires:       crate(%{pkgname}/nstextlayoutmanager)
Requires:       crate(%{pkgname}/nstextlinefragment)
Requires:       crate(%{pkgname}/nstextlist)
Requires:       crate(%{pkgname}/nstextlistelement)
Requires:       crate(%{pkgname}/nstextrange)
Requires:       crate(%{pkgname}/nstextselection)
Requires:       crate(%{pkgname}/nstextselectionnavigation)
Requires:       crate(%{pkgname}/nstextstorage)
Requires:       crate(%{pkgname}/nstextviewportlayoutcontroller)
Requires:       crate(%{pkgname}/nstoolbar-uikitadditions)
Requires:       crate(%{pkgname}/nstouchbar-uikitadditions)
Requires:       crate(%{pkgname}/nsuseractivity-nsitemprovider)
Requires:       crate(%{pkgname}/objc2-cloud-kit)
Requires:       crate(%{pkgname}/objc2-core-data)
Requires:       crate(%{pkgname}/objc2-core-foundation)
Requires:       crate(%{pkgname}/objc2-core-graphics)
Requires:       crate(%{pkgname}/objc2-core-image)
Requires:       crate(%{pkgname}/objc2-core-location)
Requires:       crate(%{pkgname}/objc2-core-text)
Requires:       crate(%{pkgname}/objc2-quartz-core)
Requires:       crate(%{pkgname}/objc2-user-notifications)
Requires:       crate(%{pkgname}/printkitui)
Requires:       crate(%{pkgname}/sharesheet)
Requires:       crate(%{pkgname}/std)
Requires:       crate(%{pkgname}/uiaccelerometer)
Requires:       crate(%{pkgname}/uiaccessibility)
Requires:       crate(%{pkgname}/uiaccessibilityadditions)
Requires:       crate(%{pkgname}/uiaccessibilityconstants)
Requires:       crate(%{pkgname}/uiaccessibilitycontainer)
Requires:       crate(%{pkgname}/uiaccessibilitycontentsizecategoryimageadjusting)
Requires:       crate(%{pkgname}/uiaccessibilitycustomaction)
Requires:       crate(%{pkgname}/uiaccessibilitycustomrotor)
Requires:       crate(%{pkgname}/uiaccessibilityelement)
Requires:       crate(%{pkgname}/uiaccessibilityidentification)
Requires:       crate(%{pkgname}/uiaccessibilitylocationdescriptor)
Requires:       crate(%{pkgname}/uiaccessibilityzoom)
Requires:       crate(%{pkgname}/uiaction)
Requires:       crate(%{pkgname}/uiactionsheet)
Requires:       crate(%{pkgname}/uiactivity)
Requires:       crate(%{pkgname}/uiactivitycollaborationmoderestriction)
Requires:       crate(%{pkgname}/uiactivityindicatorview)
Requires:       crate(%{pkgname}/uiactivityitemprovider)
Requires:       crate(%{pkgname}/uiactivityitemsconfiguration)
Requires:       crate(%{pkgname}/uiactivityitemsconfigurationreading)
Requires:       crate(%{pkgname}/uiactivityitemsconfigurationreading-sharesheet)
Requires:       crate(%{pkgname}/uiactivityviewcontroller)
Requires:       crate(%{pkgname}/uialert)
Requires:       crate(%{pkgname}/uialertcontroller)
Requires:       crate(%{pkgname}/uialertview)
Requires:       crate(%{pkgname}/uiappearance)
Requires:       crate(%{pkgname}/uiapplication)
Requires:       crate(%{pkgname}/uiapplicationshortcutitem)
Requires:       crate(%{pkgname}/uiattachmentbehavior)
Requires:       crate(%{pkgname}/uibackgroundconfiguration)
Requires:       crate(%{pkgname}/uibackgroundextensionview)
Requires:       crate(%{pkgname}/uibandselectioninteraction)
Requires:       crate(%{pkgname}/uibarappearance)
Requires:       crate(%{pkgname}/uibarbuttonitem)
Requires:       crate(%{pkgname}/uibarbuttonitemappearance)
Requires:       crate(%{pkgname}/uibarbuttonitembadge)
Requires:       crate(%{pkgname}/uibarbuttonitemgroup)
Requires:       crate(%{pkgname}/uibarcommon)
Requires:       crate(%{pkgname}/uibaritem)
Requires:       crate(%{pkgname}/uibehavioralstyle)
Requires:       crate(%{pkgname}/uibezierpath)
Requires:       crate(%{pkgname}/uiblureffect)
Requires:       crate(%{pkgname}/uibutton)
Requires:       crate(%{pkgname}/uibuttonconfiguration)
Requires:       crate(%{pkgname}/uicalendarselection)
Requires:       crate(%{pkgname}/uicalendarselectionmultidate)
Requires:       crate(%{pkgname}/uicalendarselectionsingledate)
Requires:       crate(%{pkgname}/uicalendarselectionweekofyear)
Requires:       crate(%{pkgname}/uicalendarview)
Requires:       crate(%{pkgname}/uicalendarviewdecoration)
Requires:       crate(%{pkgname}/uicanvasfeedbackgenerator)
Requires:       crate(%{pkgname}/uicellaccessory)
Requires:       crate(%{pkgname}/uicellconfigurationstate)
Requires:       crate(%{pkgname}/uicloudsharingcontroller)
Requires:       crate(%{pkgname}/uicollectionlayoutlist)
Requires:       crate(%{pkgname}/uicollectionview)
Requires:       crate(%{pkgname}/uicollectionviewcell)
Requires:       crate(%{pkgname}/uicollectionviewcompositionallayout)
Requires:       crate(%{pkgname}/uicollectionviewcontroller)
Requires:       crate(%{pkgname}/uicollectionviewflowlayout)
Requires:       crate(%{pkgname}/uicollectionviewitemregistration)
Requires:       crate(%{pkgname}/uicollectionviewlayout)
Requires:       crate(%{pkgname}/uicollectionviewlistcell)
Requires:       crate(%{pkgname}/uicollectionviewtransitionlayout)
Requires:       crate(%{pkgname}/uicollectionviewupdateitem)
Requires:       crate(%{pkgname}/uicollisionbehavior)
Requires:       crate(%{pkgname}/uicolor)
Requires:       crate(%{pkgname}/uicolorpickerviewcontroller)
Requires:       crate(%{pkgname}/uicolorwell)
Requires:       crate(%{pkgname}/uicommand)
Requires:       crate(%{pkgname}/uiconfigurationcolortransformer)
Requires:       crate(%{pkgname}/uiconfigurationstate)
Requires:       crate(%{pkgname}/uicontentconfiguration)
Requires:       crate(%{pkgname}/uicontentsizecategory)
Requires:       crate(%{pkgname}/uicontentsizecategoryadjusting)
Requires:       crate(%{pkgname}/uicontentunavailablebuttonproperties)
Requires:       crate(%{pkgname}/uicontentunavailableconfiguration)
Requires:       crate(%{pkgname}/uicontentunavailableconfigurationstate)
Requires:       crate(%{pkgname}/uicontentunavailableimageproperties)
Requires:       crate(%{pkgname}/uicontentunavailabletextproperties)
Requires:       crate(%{pkgname}/uicontentunavailableview)
Requires:       crate(%{pkgname}/uicontextmenuconfiguration)
Requires:       crate(%{pkgname}/uicontextmenuinteraction)
Requires:       crate(%{pkgname}/uicontextmenusystem)
Requires:       crate(%{pkgname}/uicontextualaction)
Requires:       crate(%{pkgname}/uicontrol)
Requires:       crate(%{pkgname}/uiconversationcontext)
Requires:       crate(%{pkgname}/uiconversationentry)
Requires:       crate(%{pkgname}/uicornerconfiguration)
Requires:       crate(%{pkgname}/uicornerradius)
Requires:       crate(%{pkgname}/uidatadetectors)
Requires:       crate(%{pkgname}/uidatasourcetranslating)
Requires:       crate(%{pkgname}/uidatepicker)
Requires:       crate(%{pkgname}/uideferredmenuelement)
Requires:       crate(%{pkgname}/uidevice)
Requires:       crate(%{pkgname}/uidiffabledatasource)
Requires:       crate(%{pkgname}/uidocument)
Requires:       crate(%{pkgname}/uidocumentbrowseraction)
Requires:       crate(%{pkgname}/uidocumentbrowserviewcontroller)
Requires:       crate(%{pkgname}/uidocumentinteractioncontroller)
Requires:       crate(%{pkgname}/uidocumentmenuviewcontroller)
Requires:       crate(%{pkgname}/uidocumentpickerextensionviewcontroller)
Requires:       crate(%{pkgname}/uidocumentpickerviewcontroller)
Requires:       crate(%{pkgname}/uidocumentproperties)
Requires:       crate(%{pkgname}/uidocumentviewcontroller)
Requires:       crate(%{pkgname}/uidocumentviewcontrollerlaunchoptions)
Requires:       crate(%{pkgname}/uidraginteraction)
Requires:       crate(%{pkgname}/uidragitem)
Requires:       crate(%{pkgname}/uidragpreview)
Requires:       crate(%{pkgname}/uidragpreviewparameters)
Requires:       crate(%{pkgname}/uidragsession)
Requires:       crate(%{pkgname}/uidropinteraction)
Requires:       crate(%{pkgname}/uidynamicanimator)
Requires:       crate(%{pkgname}/uidynamicbehavior)
Requires:       crate(%{pkgname}/uidynamicitembehavior)
Requires:       crate(%{pkgname}/uieditmenuinteraction)
Requires:       crate(%{pkgname}/uievent)
Requires:       crate(%{pkgname}/uieventattribution)
Requires:       crate(%{pkgname}/uieventattributionview)
Requires:       crate(%{pkgname}/uifeedbackgenerator)
Requires:       crate(%{pkgname}/uifieldbehavior)
Requires:       crate(%{pkgname}/uifindinteraction)
Requires:       crate(%{pkgname}/uifindsession)
Requires:       crate(%{pkgname}/uifocus)
Requires:       crate(%{pkgname}/uifocusanimationcoordinator)
Requires:       crate(%{pkgname}/uifocusdebugger)
Requires:       crate(%{pkgname}/uifocusdefines)
Requires:       crate(%{pkgname}/uifocuseffect)
Requires:       crate(%{pkgname}/uifocusguide)
Requires:       crate(%{pkgname}/uifocusmovementhint)
Requires:       crate(%{pkgname}/uifocussystem)
Requires:       crate(%{pkgname}/uifocussystem-uikitadditions)
Requires:       crate(%{pkgname}/uifocusupdatecontext-uikitadditions)
Requires:       crate(%{pkgname}/uifont)
Requires:       crate(%{pkgname}/uifontdescriptor)
Requires:       crate(%{pkgname}/uifontmetrics)
Requires:       crate(%{pkgname}/uifontpickerviewcontroller)
Requires:       crate(%{pkgname}/uifontpickerviewcontrollerconfiguration)
Requires:       crate(%{pkgname}/uifoundation)
Requires:       crate(%{pkgname}/uigeometry)
Requires:       crate(%{pkgname}/uigesturerecognizer)
Requires:       crate(%{pkgname}/uigesturerecognizersubclass)
Requires:       crate(%{pkgname}/uiglasseffect)
Requires:       crate(%{pkgname}/uigraphics)
Requires:       crate(%{pkgname}/uigraphicsimagerenderer)
Requires:       crate(%{pkgname}/uigraphicspdfrenderer)
Requires:       crate(%{pkgname}/uigraphicsrenderer)
Requires:       crate(%{pkgname}/uigraphicsrenderersubclass)
Requires:       crate(%{pkgname}/uigravitybehavior)
Requires:       crate(%{pkgname}/uiguidedaccess)
Requires:       crate(%{pkgname}/uiguidedaccessrestrictions)
Requires:       crate(%{pkgname}/uihovereffect)
Requires:       crate(%{pkgname}/uihovereffectlayer)
Requires:       crate(%{pkgname}/uihovergesturerecognizer)
Requires:       crate(%{pkgname}/uihoverstyle)
Requires:       crate(%{pkgname}/uiimage)
Requires:       crate(%{pkgname}/uiimageasset)
Requires:       crate(%{pkgname}/uiimageconfiguration)
Requires:       crate(%{pkgname}/uiimagepickercontroller)
Requires:       crate(%{pkgname}/uiimagereader)
Requires:       crate(%{pkgname}/uiimagesymbolconfiguration)
Requires:       crate(%{pkgname}/uiimageview)
Requires:       crate(%{pkgname}/uiimpactfeedbackgenerator)
Requires:       crate(%{pkgname}/uiindirectscribbleinteraction)
Requires:       crate(%{pkgname}/uiinputsuggestion)
Requires:       crate(%{pkgname}/uiinputview)
Requires:       crate(%{pkgname}/uiinputviewcontroller)
Requires:       crate(%{pkgname}/uiinteraction)
Requires:       crate(%{pkgname}/uiinterface)
Requires:       crate(%{pkgname}/uikey)
Requires:       crate(%{pkgname}/uikeyboardlayoutguide)
Requires:       crate(%{pkgname}/uikeycommand)
Requires:       crate(%{pkgname}/uikeyconstants)
Requires:       crate(%{pkgname}/uikitcore)
Requires:       crate(%{pkgname}/uikitdefines)
Requires:       crate(%{pkgname}/uilabel)
Requires:       crate(%{pkgname}/uilargecontentviewer)
Requires:       crate(%{pkgname}/uilayoutguide)
Requires:       crate(%{pkgname}/uiletterformawareadjusting)
Requires:       crate(%{pkgname}/uilexicon)
Requires:       crate(%{pkgname}/uilistcontentconfiguration)
Requires:       crate(%{pkgname}/uilistcontentimageproperties)
Requires:       crate(%{pkgname}/uilistcontenttextproperties)
Requires:       crate(%{pkgname}/uilistseparatorconfiguration)
Requires:       crate(%{pkgname}/uilocalizedindexedcollation)
Requires:       crate(%{pkgname}/uilocalnotification)
Requires:       crate(%{pkgname}/uilongpressgesturerecognizer)
Requires:       crate(%{pkgname}/uimailconversationcontext)
Requires:       crate(%{pkgname}/uimailconversationentry)
Requires:       crate(%{pkgname}/uimainmenusystem)
Requires:       crate(%{pkgname}/uimanageddocument)
Requires:       crate(%{pkgname}/uimenu)
Requires:       crate(%{pkgname}/uimenubuilder)
Requires:       crate(%{pkgname}/uimenucontroller)
Requires:       crate(%{pkgname}/uimenudisplaypreferences)
Requires:       crate(%{pkgname}/uimenuelement)
Requires:       crate(%{pkgname}/uimenuleaf)
Requires:       crate(%{pkgname}/uimenusystem)
Requires:       crate(%{pkgname}/uimessageconversationcontext)
Requires:       crate(%{pkgname}/uimessageconversationentry)
Requires:       crate(%{pkgname}/uimotioneffect)
Requires:       crate(%{pkgname}/uinavigationbar)
Requires:       crate(%{pkgname}/uinavigationbarappearance)
Requires:       crate(%{pkgname}/uinavigationcontroller)
Requires:       crate(%{pkgname}/uinavigationitem)
Requires:       crate(%{pkgname}/uinib)
Requires:       crate(%{pkgname}/uinibdeclarations)
Requires:       crate(%{pkgname}/uinibloading)
Requires:       crate(%{pkgname}/uinotificationfeedbackgenerator)
Requires:       crate(%{pkgname}/uiopenurlcontext)
Requires:       crate(%{pkgname}/uiorientation)
Requires:       crate(%{pkgname}/uipagecontrol)
Requires:       crate(%{pkgname}/uipagecontrolprogress)
Requires:       crate(%{pkgname}/uipageviewcontroller)
Requires:       crate(%{pkgname}/uipangesturerecognizer)
Requires:       crate(%{pkgname}/uipasteboard)
Requires:       crate(%{pkgname}/uipasteconfiguration)
Requires:       crate(%{pkgname}/uipasteconfigurationsupporting)
Requires:       crate(%{pkgname}/uipastecontrol)
Requires:       crate(%{pkgname}/uipencilinteraction)
Requires:       crate(%{pkgname}/uipickerview)
Requires:       crate(%{pkgname}/uipinchgesturerecognizer)
Requires:       crate(%{pkgname}/uipointeraccessory)
Requires:       crate(%{pkgname}/uipointerinteraction)
Requires:       crate(%{pkgname}/uipointerlockstate)
Requires:       crate(%{pkgname}/uipointerregion)
Requires:       crate(%{pkgname}/uipointerstyle)
Requires:       crate(%{pkgname}/uipopoverbackgroundview)
Requires:       crate(%{pkgname}/uipopovercontroller)
Requires:       crate(%{pkgname}/uipopoverpresentationcontroller)
Requires:       crate(%{pkgname}/uipopoverpresentationcontrollersourceitem)
Requires:       crate(%{pkgname}/uipopoversupport)
Requires:       crate(%{pkgname}/uipresentationcontroller)
Requires:       crate(%{pkgname}/uipress)
Requires:       crate(%{pkgname}/uipressesevent)
Requires:       crate(%{pkgname}/uipreviewinteraction)
Requires:       crate(%{pkgname}/uipreviewparameters)
Requires:       crate(%{pkgname}/uiprinter)
Requires:       crate(%{pkgname}/uiprinterpickercontroller)
Requires:       crate(%{pkgname}/uiprinterror)
Requires:       crate(%{pkgname}/uiprintformatter)
Requires:       crate(%{pkgname}/uiprintinfo)
Requires:       crate(%{pkgname}/uiprintinteractioncontroller)
Requires:       crate(%{pkgname}/uiprintpagerenderer)
Requires:       crate(%{pkgname}/uiprintpaper)
Requires:       crate(%{pkgname}/uiprintserviceextension)
Requires:       crate(%{pkgname}/uiprogressview)
Requires:       crate(%{pkgname}/uipushbehavior)
Requires:       crate(%{pkgname}/uireferencelibraryviewcontroller)
Requires:       crate(%{pkgname}/uirefreshcontrol)
Requires:       crate(%{pkgname}/uiregion)
Requires:       crate(%{pkgname}/uiresponder)
Requires:       crate(%{pkgname}/uiresponder-uiactivityitemsconfiguration)
Requires:       crate(%{pkgname}/uirotationgesturerecognizer)
Requires:       crate(%{pkgname}/uiscene)
Requires:       crate(%{pkgname}/uiscene-avaudiosession)
Requires:       crate(%{pkgname}/uisceneactivationconditions)
Requires:       crate(%{pkgname}/uisceneconfiguration)
Requires:       crate(%{pkgname}/uiscenedefinitions)
Requires:       crate(%{pkgname}/uiscenedestructioncondition)
Requires:       crate(%{pkgname}/uisceneenhancedstaterestoration)
Requires:       crate(%{pkgname}/uisceneoptions)
Requires:       crate(%{pkgname}/uiscenesession)
Requires:       crate(%{pkgname}/uiscenesessionactivationrequest)
Requires:       crate(%{pkgname}/uiscenesizerestrictions)
Requires:       crate(%{pkgname}/uiscenesystemprotectionmanager)
Requires:       crate(%{pkgname}/uiscenewindowingbehaviors)
Requires:       crate(%{pkgname}/uiscenewindowingcontrolstyle)
Requires:       crate(%{pkgname}/uiscreen)
Requires:       crate(%{pkgname}/uiscreenedgepangesturerecognizer)
Requires:       crate(%{pkgname}/uiscreenmode)
Requires:       crate(%{pkgname}/uiscreenshotservice)
Requires:       crate(%{pkgname}/uiscribbleinteraction)
Requires:       crate(%{pkgname}/uiscrolledgeelementcontainerinteraction)
Requires:       crate(%{pkgname}/uiscrollview)
Requires:       crate(%{pkgname}/uisearchbar)
Requires:       crate(%{pkgname}/uisearchcontainerviewcontroller)
Requires:       crate(%{pkgname}/uisearchcontroller)
Requires:       crate(%{pkgname}/uisearchdisplaycontroller)
Requires:       crate(%{pkgname}/uisearchsuggestion)
Requires:       crate(%{pkgname}/uisearchtab)
Requires:       crate(%{pkgname}/uisearchtextfield)
Requires:       crate(%{pkgname}/uisegmentedcontrol)
Requires:       crate(%{pkgname}/uiselectionfeedbackgenerator)
Requires:       crate(%{pkgname}/uishadowproperties)
Requires:       crate(%{pkgname}/uishape)
Requires:       crate(%{pkgname}/uisheetpresentationcontroller)
Requires:       crate(%{pkgname}/uislider)
Requires:       crate(%{pkgname}/uislidertrackconfiguration)
Requires:       crate(%{pkgname}/uismartreplysuggestion)
Requires:       crate(%{pkgname}/uisnapbehavior)
Requires:       crate(%{pkgname}/uisplitviewcontroller)
Requires:       crate(%{pkgname}/uisplitviewcontrollerlayoutenvironment)
Requires:       crate(%{pkgname}/uispringloadedinteraction)
Requires:       crate(%{pkgname}/uispringloadedinteractionsupporting)
Requires:       crate(%{pkgname}/uistackview)
Requires:       crate(%{pkgname}/uistandardtextcursorview)
Requires:       crate(%{pkgname}/uistaterestoration)
Requires:       crate(%{pkgname}/uistatusbarmanager)
Requires:       crate(%{pkgname}/uistepper)
Requires:       crate(%{pkgname}/uistoryboard)
Requires:       crate(%{pkgname}/uistoryboardpopoversegue)
Requires:       crate(%{pkgname}/uistoryboardsegue)
Requires:       crate(%{pkgname}/uistringdrawing)
Requires:       crate(%{pkgname}/uiswipeactionsconfiguration)
Requires:       crate(%{pkgname}/uiswipegesturerecognizer)
Requires:       crate(%{pkgname}/uiswitch)
Requires:       crate(%{pkgname}/uisymbolcontenttransition)
Requires:       crate(%{pkgname}/uisymboleffectcompletion)
Requires:       crate(%{pkgname}/uitab)
Requires:       crate(%{pkgname}/uitabaccessory)
Requires:       crate(%{pkgname}/uitabbar)
Requires:       crate(%{pkgname}/uitabbarappearance)
Requires:       crate(%{pkgname}/uitabbarcontroller)
Requires:       crate(%{pkgname}/uitabbarcontrollersidebar)
Requires:       crate(%{pkgname}/uitabbaritem)
Requires:       crate(%{pkgname}/uitabgroup)
Requires:       crate(%{pkgname}/uitableview)
Requires:       crate(%{pkgname}/uitableviewcell)
Requires:       crate(%{pkgname}/uitableviewcontroller)
Requires:       crate(%{pkgname}/uitableviewheaderfooterview)
Requires:       crate(%{pkgname}/uitabsidebaritem)
Requires:       crate(%{pkgname}/uitapgesturerecognizer)
Requires:       crate(%{pkgname}/uitargeteddragpreview)
Requires:       crate(%{pkgname}/uitargetedpreview)
Requires:       crate(%{pkgname}/uitextchecker)
Requires:       crate(%{pkgname}/uitextcursordroppositionanimator)
Requires:       crate(%{pkgname}/uitextcursorview)
Requires:       crate(%{pkgname}/uitextdragging)
Requires:       crate(%{pkgname}/uitextdragpreviewrenderer)
Requires:       crate(%{pkgname}/uitextdragurlpreviews)
Requires:       crate(%{pkgname}/uitextdropping)
Requires:       crate(%{pkgname}/uitextdropproposal)
Requires:       crate(%{pkgname}/uitextfield)
Requires:       crate(%{pkgname}/uitextformattingcoordinator)
Requires:       crate(%{pkgname}/uitextformattingviewcontroller)
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerchangevalue)
Requires:       crate(%{pkgname}/uitextformattingviewcontrollercomponent)
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerconfiguration)
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerformattingdescriptor)
Requires:       crate(%{pkgname}/uitextformattingviewcontrollerformattingstyle)
Requires:       crate(%{pkgname}/uitextinput)
Requires:       crate(%{pkgname}/uitextinputcontext)
Requires:       crate(%{pkgname}/uitextinputtraits)
Requires:       crate(%{pkgname}/uitextinteraction)
Requires:       crate(%{pkgname}/uitextitem)
Requires:       crate(%{pkgname}/uitextiteminteraction)
Requires:       crate(%{pkgname}/uitextloupesession)
Requires:       crate(%{pkgname}/uitextpasteconfigurationsupporting)
Requires:       crate(%{pkgname}/uitextpastedelegate)
Requires:       crate(%{pkgname}/uitextsearching)
Requires:       crate(%{pkgname}/uitextselectiondisplayinteraction)
Requires:       crate(%{pkgname}/uitextselectionhandleview)
Requires:       crate(%{pkgname}/uitextselectionhighlightview)
Requires:       crate(%{pkgname}/uitextview)
Requires:       crate(%{pkgname}/uitimingcurveprovider)
Requires:       crate(%{pkgname}/uitimingparameters)
Requires:       crate(%{pkgname}/uitoolbar)
Requires:       crate(%{pkgname}/uitoolbarappearance)
Requires:       crate(%{pkgname}/uitooltipinteraction)
Requires:       crate(%{pkgname}/uitouch)
Requires:       crate(%{pkgname}/uitrackinglayoutguide)
Requires:       crate(%{pkgname}/uitrait)
Requires:       crate(%{pkgname}/uitraitcollection)
Requires:       crate(%{pkgname}/uitraitlistenvironment)
Requires:       crate(%{pkgname}/uiupdateactionphase)
Requires:       crate(%{pkgname}/uiupdateinfo)
Requires:       crate(%{pkgname}/uiupdatelink)
Requires:       crate(%{pkgname}/uiuseractivity)
Requires:       crate(%{pkgname}/uiusernotificationsettings)
Requires:       crate(%{pkgname}/uivibrancyeffect)
Requires:       crate(%{pkgname}/uivideoeditorcontroller)
Requires:       crate(%{pkgname}/uiview)
Requires:       crate(%{pkgname}/uiviewanimating)
Requires:       crate(%{pkgname}/uiviewconfigurationstate)
Requires:       crate(%{pkgname}/uiviewcontroller)
Requires:       crate(%{pkgname}/uiviewcontrollertransition)
Requires:       crate(%{pkgname}/uiviewcontrollertransitioncoordinator)
Requires:       crate(%{pkgname}/uiviewcontrollertransitioning)
Requires:       crate(%{pkgname}/uiviewlayoutregion)
Requires:       crate(%{pkgname}/uiviewpropertyanimator)
Requires:       crate(%{pkgname}/uivisualeffect)
Requires:       crate(%{pkgname}/uivisualeffectview)
Requires:       crate(%{pkgname}/uiwebview)
Requires:       crate(%{pkgname}/uiwindow)
Requires:       crate(%{pkgname}/uiwindowscene)
Requires:       crate(%{pkgname}/uiwindowsceneactivationaction)
Requires:       crate(%{pkgname}/uiwindowsceneactivationconfiguration)
Requires:       crate(%{pkgname}/uiwindowsceneactivationinteraction)
Requires:       crate(%{pkgname}/uiwindowsceneactivationrequestoptions)
Requires:       crate(%{pkgname}/uiwindowscenedraginteraction)
Requires:       crate(%{pkgname}/uiwindowscenegeometry)
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferences)
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesios)
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesmac)
Requires:       crate(%{pkgname}/uiwindowscenegeometrypreferencesvision)
Requires:       crate(%{pkgname}/uiwindowsceneplacement)
Requires:       crate(%{pkgname}/uiwindowsceneprominentplacement)
Requires:       crate(%{pkgname}/uiwindowscenepushplacement)
Requires:       crate(%{pkgname}/uiwindowscenereplaceplacement)
Requires:       crate(%{pkgname}/uiwindowscenestandardplacement)
Requires:       crate(%{pkgname}/uiwritingtoolscoordinator)
Requires:       crate(%{pkgname}/uiwritingtoolscoordinatoranimationparameters)
Requires:       crate(%{pkgname}/uiwritingtoolscoordinatorcontext)
Requires:       crate(%{pkgname}/uizoomtransitionoptions)
Requires:       crate(%{pkgname}/unnotificationresponse-uikitadditions)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-cloud-kit
Summary:        Bindings to the UIKit framework - feature "objc2-cloud-kit"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-cloud-kit-0.3/ckcontainer) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckrecord) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckshare) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/cksharemetadata) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-cloud-kit)

%description -n %{name}+objc2-cloud-kit
This metapackage enables feature "objc2-cloud-kit" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-data
Summary:        Bindings to the UIKit framework - feature "objc2-core-data"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-data-0.3/nsmanagedobjectcontext) >= 0.3.2
Requires:       crate(objc2-core-data-0.3/nsmanagedobjectmodel) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-data)

%description -n %{name}+objc2-core-data
This metapackage enables feature "objc2-core-data" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-foundation
Summary:        Bindings to the UIKit framework - feature "objc2-core-foundation"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-foundation-0.3/cfcgtypes) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/cfdate) >= 0.3.2
Requires:       crate(objc2-core-foundation-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-foundation)

%description -n %{name}+objc2-core-foundation
This metapackage enables feature "objc2-core-foundation" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-graphics
Summary:        Bindings to the UIKit framework - feature "objc2-core-graphics"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-graphics-0.3/cgcolor) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgcontext) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgfont) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgimage) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/cgpath) >= 0.3.2
Requires:       crate(objc2-core-graphics-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-graphics)

%description -n %{name}+objc2-core-graphics
This metapackage enables feature "objc2-core-graphics" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-image
Summary:        Bindings to the UIKit framework - feature "objc2-core-image"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-image-0.3/cicolor) >= 0.3.2
Requires:       crate(objc2-core-image-0.3/ciimage) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-image)

%description -n %{name}+objc2-core-image
This metapackage enables feature "objc2-core-image" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-location
Summary:        Bindings to the UIKit framework - feature "objc2-core-location"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-location-0.3/clregion) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-location)

%description -n %{name}+objc2-core-location
This metapackage enables feature "objc2-core-location" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-text
Summary:        Bindings to the UIKit framework - feature "objc2-core-text"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-text-0.3/ctfont) >= 0.3.2
Requires:       crate(objc2-core-text-0.3/ctfontdescriptor) >= 0.3.2
Requires:       crate(objc2-core-text-0.3/objc2) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-text)

%description -n %{name}+objc2-core-text
This metapackage enables feature "objc2-core-text" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-quartz-core
Summary:        Bindings to the UIKit framework - feature "objc2-quartz-core"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-quartz-core-0.3/cadisplaylink) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/caframeraterange) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/calayer) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/camediatiming) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/catransform3d) >= 0.3.2
Requires:       crate(objc2-quartz-core-0.3/objc2-core-foundation) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-quartz-core)

%description -n %{name}+objc2-quartz-core
This metapackage enables feature "objc2-quartz-core" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-symbols
Summary:        Bindings to the UIKit framework - feature "objc2-symbols"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-symbols-0.3/nssymboleffect) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-symbols)

%description -n %{name}+objc2-symbols
This metapackage enables feature "objc2-symbols" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-uniform-type-identifiers
Summary:        Bindings to the UIKit framework - feature "objc2-uniform-type-identifiers"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-uniform-type-identifiers-0.3/uttype) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-uniform-type-identifiers)

%description -n %{name}+objc2-uniform-type-identifiers
This metapackage enables feature "objc2-uniform-type-identifiers" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-user-notifications
Summary:        Bindings to the UIKit framework - feature "objc2-user-notifications"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-user-notifications-0.3/unnotificationresponse) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-user-notifications)

%description -n %{name}+objc2-user-notifications
This metapackage enables feature "objc2-user-notifications" for the Rust objc2-ui-kit crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
