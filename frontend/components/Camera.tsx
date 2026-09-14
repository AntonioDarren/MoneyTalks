"use client";

import { Strait } from "next/font/google";
import { use, useEffect, useRef, useState } from "react";

type Prediction = {
    denomination: number | null;
    confidence: number;
    box?: number[] | null;
};

export default function Camera(){
    const videoRef = useRef<HTMLVideoElement | null>(null);
    const canvasRef = useRef<HTMLCanvasElement | null>(null);
    const streamRef = useRef<MediaStream | null>(null);

    const [cameraStarted, setCameraStarted] = useState(false);
    const [loading, setLoading] = useState(false);
    const [prediction, setPrediction] = useState<Prediction | null>(null);
    const [error, setError] = useState("");

    useEffect(() => {
        return () => {
            streamRef.current?.getTracks().forEach((track) => track.stop());
        };
    }, []);

    async function startCamera() {
        try {
            setError("");
            const stream = await navigator.mediaDevices.getUserMedia({
                video: {
                    facingMode: { ideal: "environment" },
                    width: { ideal: 1280 },
                    height: { ideal: 720 } 
                },
                audio: false
            });

            streamRef.current = stream;

            if (videoRef.current) {
                videoRef.current.srcObject = stream;
            }

            setCameraStarted(true);
        } catch(err) {
            console.error(err);
            setError("Couldn't access the camera")
        }
    }
}

