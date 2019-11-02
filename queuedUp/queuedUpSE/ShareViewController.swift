//
//  ShareViewController.swift
//  queuedUpSE
//
//  Created by Alex Haight on 11/1/19.
//  Copyright © 2019 Alex Haight. All rights reserved.
//

import UIKit
import Social
import MobileCoreServices

class ShareViewController: SLComposeServiceViewController {

    override func isContentValid() -> Bool {
        // Do validation of contentText and/or NSExtensionContext attachments here
        return true
    }

    override func didSelectPost() {
        // This is called after the user selects Post. Do the upload of contentText and/or NSExtensionContext attachments.
    
        // Inform the host that we're done, so it un-blocks its UI. Note: Alternatively you could call super's -didSelectPost, which will similarly complete the extension context.
        //let url = URL(string: "https://ptsv2.com/t/ngiaa-1572674328/post")!
        //var request = URLRequest(url: url)
        self.extensionContext!.completeRequest(returningItems: [], completionHandler: nil)
        let content = self.extensionContext!.inputItems[0] as! NSExtensionItem
        if let item = extensionContext?.inputItems.first as? NSExtensionItem {
            if let itemProvider = item.attachments?.first as? NSItemProvider {
                if itemProvider.hasItemConformingToTypeIdentifier("public.url") {
                    itemProvider.loadItem(forTypeIdentifier: "public.url", options: nil, completionHandler: { (url, error) -> Void in
                        if let shareURL = url as? NSURL {
                            print (shareURL.absoluteString!);
                            let newURL: String = shareURL.absoluteString!;
                            let url = URL(string: "https://ptsv2.com/t/yjn0q-1572713140/post")!
                            var request = URLRequest(url: url)
                            request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
                            request.httpMethod = "POST"
                            request.httpBody = newURL.data(using: .utf8);

                            let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
                                guard let data = data else { return }
                                print(String(data: data, encoding: .utf8)!)
                            }

                            task.resume()
                        }
                    }
                )}
            }
        }
    }

    override func configurationItems() -> [Any]! {
        // To add configuration options via table cells at the bottom of the sheet, return an array of SLComposeSheetConfigurationItem here.
        return []
    }

}
